import threading
from github_services.base_request import BaseRequest


class GithubService:
    _session_instance = None
    _session_lock = threading.Lock()

    def __init__(self):
        self.base_request = BaseRequest()

    @classmethod
    def instance(cls):
        if not cls._session_instance:
            with cls._session_lock:
                if not cls._session_instance:
                    cls._session_instance = cls()
        return cls._session_instance
