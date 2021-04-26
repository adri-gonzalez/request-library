from github_services.rest_interceptor import rest_service
from utils.constants.service_methods import ServiceMethods as Type


class UserApi:
    @staticmethod
    @rest_service(url="/users", http_method=Type.GET)
    def get_users(): pass
