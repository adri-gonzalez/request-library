import requests
import threading


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
