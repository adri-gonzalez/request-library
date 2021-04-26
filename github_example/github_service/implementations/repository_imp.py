from github_example.github_service.apis.repository_api import RepositoryApi


class RepositoryFlow:
    @staticmethod
    def get_repositories():
        return RepositoryApi.get_repositories()
