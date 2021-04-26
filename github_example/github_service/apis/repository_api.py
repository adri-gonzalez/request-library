from github_example.github_service.rest_interceptor import rest_service
from github_example.utils.constants.service_methods import ServiceMethods as Type


class RepositoryApi:
    @staticmethod
    @rest_service(url="/repos", http_method=Type.GET)
    def get_repositories(): pass

