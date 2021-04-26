from github_example.github_service.github_service import GithubService
import re

_all__ = ['rest_service']


def rest_service(url, http_method, query_string=None, header_params=None, default_payload=None):
    def decorator(func):
        def wrapper(payload={}, query_string_values={}, url_params={}, header_params_values={}):
            complete_url = url
            qs_params = None
            payload_f = default_payload
            if re.findall("({\w+})+", url):
                complete_url = url.format_map(url_params)
            if query_string is not None:
                qs_params = _check_query_string(query_string, query_string_values)
            if payload is not None:
                payload_f = payload
            service = GithubService.instance().base_request
            return service.execute_request(
                lambda: service.request(http_method, complete_url, params=qs_params, json=payload_f))

        return wrapper

    return decorator


# def rest_service(url, http_method, query_string=None, header_params=None, default_payload=None):
#     def decorator(func):
#         def wrapper(payload={}, query_string_values={}, url_params={}, header_params_values={}):
#             qs_params = None
#             payload_f = default_payload
#             if re.findall("({\w+})+", url):
#                 complete_url = url.format_map(url_params)
#             if query_string is not None:
#                 qs_params = _check_query_string(query_string, query_string_values)
#             if payload is not None:
#                 payload_f = payload
#             service = GithubService.instance().base_request
#             return service.execute_request(
#                 lambda c: service.request(http_method, complete_url, cookies=c, params=qs_params, json=payload_f))
#
#         return wrapper
#
#     return decorator


def _check_query_string(query_string, query_string_values):
    new_dict = {}
    for key, value in query_string.items():
        if ('required' in value) and value['required'] == True:
            new_dict[key] = query_string_values[key]
            continue
        if ('required' in value) and value['required'] == False:
            if key in query_string_values.keys():
                new_dict[key] = query_string_values[key]
            continue
        new_dict[key] = value['default']
    return new_dict
