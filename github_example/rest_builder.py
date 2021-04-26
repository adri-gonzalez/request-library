from github_example.session_factory import RestSessionFactory


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
