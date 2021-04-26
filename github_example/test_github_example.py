# from github_example.github_service.implementations.repository_imp import RepositoryFlow
# from github_example.utils.load_env import load_dotenv
#
# load_dotenv()
# response = RepositoryFlow.get_repositories()
import requests
import threading
import re


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


def rest_service(url, http_method, query_string=None, header_params=None, default_payload=None):
    def decorator(func):
        def wrapper(payload={}, query_string_values={}, url_params={}, header_params_values={}):
            complete_url = url
            qs_params = None
            payload_f = default_payload
            if re.findall("({\w+})+", url):
                complete_url = url.format_map(url_params)
            if query_string is not None:
                qs_params = _check_query_string(query_string, query_string_values)
            if payload is not None:
                payload_f = payload
            service = GitHubService._rest_instance().base_request
            return service.execute_request(
                lambda: service.request(http_method, complete_url, params=qs_params, json=payload_f))

        return wrapper

    return decorator


def _check_query_string(query_string, query_string_values):
    new_dict = {}
    for key, value in query_string.items():
        if ('required' in value) and value['required'] == True:
            new_dict[key] = query_string_values[key]
            continue
        if ('required' in value) and value['required'] == False:
            if key in query_string_values.keys():
                new_dict[key] = query_string_values[key]
            continue
        new_dict[key] = value['default']
    return new_dict


class GitHubService(RestBuilder):
    def __init__(self):
        super().__init__(base_url='https://api.github.com',
                         headers={'Authorization': 'token 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'})


class RepositoryApi:
    @staticmethod
    @rest_service(url="/repos", http_method='get')
    def get_repositories(): pass


class RepositoryFlow:
    @staticmethod
    def get_repositories():
        return RepositoryApi.get_repositories()


response = RepositoryFlow.get_repositories()
print(response)
