from github_example.utils.load_env import load_dotenv
from github_example.github_service.implementations.user_imp import UserApi

load_dotenv()
get_users_resp = UserApi.get_users()
print(get_users_resp)
