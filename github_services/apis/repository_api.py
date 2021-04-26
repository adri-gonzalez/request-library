from github_services.rest_interceptor import rest_service
from utils.constants.service_methods import ServiceMethods as Type


class RepositoryApi:
    @staticmethod
    @rest_service(url="/user/repos", http_method=Type.POST)
    def create_repository(payload): pass
