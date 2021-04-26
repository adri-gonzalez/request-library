from github_services.apis.users_api import UserApi


class UserFlow:
    @staticmethod
    def get_users():
        return UserApi.get_users()
