import os
from rest_builder import RestBuilder


class BaseRequest(RestBuilder):
    def __init__(self, username=None, token=None):
        if username is None:
            self.username = os.getenv('USERNAME')
        if token is None:
            self.token = os.getenv('TOKEN')
        super().__init__(base_url='https://api.github.com',
                         headers={'Authorization': f'token {os.getenv("TOKEN")}',
                                  'Content-Type': 'application/json'})

    def execute_request(self, request):
        return request().json()
