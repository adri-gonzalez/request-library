from github_example.github_service.apis.users_api import UserApi


class RepositoryFlow:
    @staticmethod
    def get_repositories():
        return UserApi.get_users()
