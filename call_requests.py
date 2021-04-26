from utils.load_env import load_dotenv
from github_services.implementations.user_imp import UserFlow
from github_services.implementations.query_imp import QueryFlow
from github_services.implementations.repository_imp import RepositoryFlow

load_dotenv()
print('################# CREATE A NEW REPOSITORY ################')
create_repository = RepositoryFlow.create_repositories(repository_model={
    "name": "other private rpository",
    "description": "This is your first repository",
    "homepage": "https://github.com",
    "private": False,
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True
})
print(create_repository)

print('################# GET USER INFORMATION ################')
get_user_data = UserFlow.get_users()
print(get_user_data)

print('################# GET REPOSITORIES ################')
query_repository = QueryFlow.get_repositories('adri-gonzalez')
print(query_repository)
