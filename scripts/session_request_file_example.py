import requests
import threading
import json


class RestSessionFactory:
    _session_lock = threading.Lock()
    _session_instance = None

    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self._parse_arguments(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    @classmethod
    def instance(cls, base_url, **kwargs):
        if not cls._session_instance:
            with cls._session_lock:
                if not cls._session_instance:
                    cls._session_instance = cls(base_url, **kwargs)
        return cls._session_instance

    @staticmethod
    def _parse_arguments(source, destination):
        for key, value in source.items():
            if isinstance(value, dict):
                node = destination.setdefault(key, {})
                RestSessionFactory._parse_arguments(value, node)
            else:
                destination[key] = value
        return destination


class RestBuilder:
    _rest_instance = None

    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self._rest_instance = RestSessionFactory.instance(base_url, **kwargs)

    def request(self, method, url, **kwargs):
        return self._rest_instance.session.request(method, self.base_url + url, **kwargs)

    def head(self, url, **kwargs):
        return self._rest_instance.session.head(self.base_url + url, **kwargs)

    def get(self, url, **kwargs):
        return self._rest_instance.session.get(self.base_url + url, **kwargs)

    def post(self, url, **kwargs):
        return self._rest_instance.session.post(self.base_url + url, **kwargs)

    def put(self, url, **kwargs):
        return self._rest_instance.session.put(self.base_url + url, **kwargs)

    def patch(self, url, **kwargs):
        return self._rest_instance.session.patch(self.base_url + url, **kwargs)

    def delete(self, url, **kwargs):
        return self._rest_instance.session.delete(self.base_url + url, **kwargs)


class ServiceMethods:
    POST = 'post'
    PUT = 'put'
    GET = 'get'
    DELETE = 'delete'
    HEAD = 'head'
    PATCH = 'patch'


class GitHubService(RestBuilder):
    def __init__(self):
        super().__init__(base_url='https://api.github.com',
                         headers={'Authorization': 'token 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',
                                  'Content-Type': 'application/json'})


# CREATE GITHUB SERVICE
github_service = GitHubService()

# GET GITHUB USER:
get_user_response = github_service.request(ServiceMethods.GET, url='/users')

# CREATE REPOSITORY
create_repository_response_json = github_service.request(ServiceMethods.POST, url='/user/repos',
                                                         json={"name": "new-repository-api",
                                                               "description": "This is your first repository",
                                                               "homepage": "https://github.com",
                                                               "private": True,
                                                               "has_issues": True,
                                                               "has_projects": True,
                                                               "has_wiki": True})

# CREATE REPOSITORY
create_repository_response_data = github_service.request(ServiceMethods.POST, url='/user/repos',
                                                         data=json.dumps({"name": "new-repository-api",
                                                                          "description": "This is your first repository",
                                                                          "homepage": "https://github.com",
                                                                          "private": True,
                                                                          "has_issues": True,
                                                                          "has_projects": True,
                                                                          "has_wiki": True}))
