from github_services.apis.query_api import QueryApi


class QueryFlow:
    @staticmethod
    def get_repositories(owner):
        return QueryApi.query_github(url_params={'owner': owner})
