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

    # def execute_request(self, request):
    #     self._authenticate_user()
    #     response = request(self.auth_cookies)
    #     assert_that(response.status_code).is_equal_to(200)
    #     assert_that(response.content).is_not_none()
    #     return response.json()

    # def _authenticate_user(self):
    #     user = {
    #         'username': '',
    #         'token': ''
    #     }
    #     auth_response = self.post('/login', auth=user)
    #     assert_that(auth_response).is_not_none()
    #     self.auth_cookies = self._validate_and_get_cookies(auth_response)

    # @staticmethod
    # def _validate_and_get_cookies(auth):
    #     auth_cookies = auth.cookies
    #     assert_that(auth_cookies).is_not_none()
    #     api_cookies = auth_cookies.get_dict()
    #     assert_that(api_cookies).is_not_none()
    #     return auth_cookies
