from github_services.rest_interceptor import rest_service
from utils.constants.service_methods import ServiceMethods as Type


class QueryApi:
    @staticmethod
    @rest_service(url="/{owner}", http_method=Type.GET, query_string={
        'tab': {'default': "repositories"},
        'q': {'default': ""},
        'type': {'default': "public"},
        'language': {'default': ""},
        'sort': {'default': ""},
    })
    def query_github(url_params, query_string_values): pass
