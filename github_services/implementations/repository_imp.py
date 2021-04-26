from github_services.apis.repository_api import RepositoryApi


class RepositoryFlow:
    @staticmethod
    def create_repositories(repository_model):
        return RepositoryApi.create_repository(payload=repository_model)
