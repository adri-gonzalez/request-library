"""
    Commands
        GET
            Leer un recurso existente. Esto es como SELECT en SQL
        HEAD
            Similar a GET, excepto que el servidor no devuelve un cuerpo de mensaje en
            respuesta. En cambio, obtiene los metadatos de un recurso existente.
        POST
            Crea un nuevo recurso. Esto es como INSERT en SQL
        PUT
            Actualiza un recurso existente. Esto es como ACTUALIZAR en SQL
        PATCH
            Generalmente no implementado. Actualiza parte de un recurso existente.
            Esto es como ACTUALIZAR en SQL
        DELETE
            Elimina un recurso existente. Esto es como BORRAR en SQL
    Important HTTP Status Codes
        200 OK significa éxito
            GET: devuelve el recurso
            PUT: proporciona un mensaje de estado o devuelve un mensaje
        201 Creado significa éxito
            POST: proporciona un mensaje de estado o devuelve un recurso recién creado
        204 Sin contenido significa éxito
            Completado, pero nada para devolver (debido a que no hay contenido)
        304 Sin cambios significa Redirigir
            No hay cambios desde la última solicitud (generalmente se usa para verificar un campo como los encabezados 'Última modificación' y 'Etag', que es un mecanismo para la validación de la caché web)
        400 Solicitud incorrecta significa falla
            PUT: devuelve un mensaje de error, incluidos los errores de validación del formulario
            POST: devuelve un mensaje de error, incluidos los errores de validación del formulario
        401 No autorizado significa Fallo
            Se requiere autenticación, pero el usuario no proporcionó las credenciales.
        403 Prohibido significa Fracaso
            El usuario intentó acceder a contenido restringido
        404 No encontrado significa falla
            No se encontró el recurso
        405 Método no permitido significa falla
            Se intentó un método HTTP no válido
        410 Ido significa fracaso
            Se intentó un método que ya no es compatible.
            P.ej. Las aplicaciones móviles pueden probar esta condición y, si ocurre,
                 decirle al usuario que actualice
        500 Error interno del servidor significa falla
            El servidor encontró una condición inesperada
    Sample API URLS
        api / v1 / resume
            para GET y POST
        api / v1 / resume /: slug /
            para OBTENER, PONER, ELIMINAR
        api / v1 / trabajo
            para GET y POST
        api / v1 / job /: slug /
            para OBTENER, PONER, ELIMINAR
        Lo mismo ocurre con api / v1 / education y api / v1 / experience
        slug representa una variable (por ejemplo, la identificación del currículum)
"""

import json
import requests


def get_webpage_details(site):
    """ GET details of a request """
    r = requests.get(site)

    # Status Code
    print("GET Response Status Code: ", r.status_code)  # 200

    print(r.headers)  # Gets all headers as a dict
    """
    {
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
    }
    """

    print("Get specific field (e.g. 'content-type'):", r.headers['content-type'])  # Get specific field
    # application/json; charset=utf-8

    print("Get encoding: ", r.encoding)  # utf-8

    # print "Get Text: ", r.text  # Get all text of page
    # print "Get JSON: ", r.json()  # Get everything as a JSON file


def request_API_calls():
    """ Using all HTTP request types (POST, PUT, DELETE, HEAD, OPTIONS) """
    r = requests.post('http://httpbin.org/post')  # Example of POST
    print("POST: ", r)  # <Response [200]>
    r = requests.put('http://httpbin.org/put')  # Example of PUT
    print("PUT: ", r)  # <Response [200]>
    r = requests.delete('http://httpbin.org/delete')  # Example of DELETE
    print("DELETE: ", r)  # <Response [200]>
    r = requests.head('http://httpbin.org/get')  # Example of HEAD
    print("HEAD: ", r)  # <Response [200]>
    r = requests.options('http://httpbin.org/get')  # Example of OPTIONS
    print("OPTIONS: ", r)  # <Response [200]>


def pass_params_in_urls():
    """
        How to pass data in the URL's query string
        By hand, getting URL would be given as key/value pairs in the URL
        after the question mark (e.g. httpbin.org/get?key=val), but instead
        we have a 'params' that we can pass a dict into
    """

    # If you want to pass 'key1=value1' and 'key2=value2' to 'httpbin.org/get'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params=payload)

    # Again, this is the same as http://httpbin.org/get?key2=value2&key1=value1

    # Verify that URL has been encoded correctly by printing out URL
    print("URL is: ", r.url)  # http://httpbin.org/get?key2=value2&key1=value1


def post_form_data_request():
    """
        If you want to send form-encoded data (like an HTML form), then
        pass a dictionary to the 'data' argument; the dict will be auto form
        encoded when the request is made
    """
    url = "http://httpbin.org/post"
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=payload)
    print(r.text)  # see how data goes into 'form'

    """
    {
      "args": {},
      "data": "",
      "files": {},
      "form": {
        "key1": "value1",
        "key2": "value2"
      },
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "23",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.5.3 CPython/2.7.9 Darwin/14.1.0"
      },
      "json": null,
      "origin": "74.71.230.126",
      "url": "http://httpbin.org/post"
    }
    """

    # If you want to send data that is not form-encoded, pass in a string
    payload = 'This is a test'
    r = requests.post(url, data=payload)
    print(r.text)  # see how it goes to 'data' instead of 'form'

    """
    {
      "args": {},
      "data": "This is a test",
      "files": {},
      "form": {},
      "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "14",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.5.3 CPython/2.7.9 Darwin/14.1.0"
      },
      "json": null,
      "origin": "74.71.230.126",
      "url": "http://httpbin.org/post"
    }
    """


def pass_headers_in_request():
    """
        Add HTTP headers to a request by adding a dict to the 'headers' param
    """
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r)


def response_content():
    """ We can read the server's response """
    r = requests.get('https://developer.github.com/v3/activity/events/#list-public-events')
    print("Server's Response is: ", r.text)

    # When you make a request, Requests makes an educated guess on encoding
    # based on the response of the HTTP headers
    print("Guessed encoding is: ", r.encoding)  # utf-8
    # print "Peak at content if unsure of encoding, sometimes specified in here ", r.content


def json_response_content():
    """ There's a builtin JSON decoder for dealing with JSON data """
    r = requests.get('http://www.json-generator.com/api/json/get/bVVKnZVjpK?indent=2')
    print("Getting JSON: ", r)  # Should be 200 or else if error, then 401 (Unauthorized)
    # print r.json()


def versatile_response_codes():
    """ You don't have to check for specific status codes (e.g. 200, 404) """
    url = "http://httpbin.org/post"
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print("Looks okay to me", r.status_code)
    else:
        print("Doesn't look good here", r.status_code)

        # We can raise an exception if there's a bad request 4XX or 5XX
        r.raise_for_status()  # Should raise http_error
        # (requests.exceptions.HTTPError:)


def accessing_cookies():
    """
        You can look at a response's cookies or send your own cookies
        to the server
    """
    # GET some cookies
    url = 'http://example.com/some/cookie/setting/url'
    r = requests.get(url)
    r.cookies['example_cookie_name']  # 'example_cookie_value'

    # GET and specify your cookies
    my_cookies = dict(cookies_are='working')
    r = requests.get(url, cookies=my_cookies)
    print(r.text)  # '{"cookies": { "cookies_are": "working"}}'


def request_no_redirect():
    """
        By default Requests will perform redirects for all verbs except HEAD
        Use the 'history' property of the Response to track redirection
        Response.history list contains all the Response objects that
        were created (sorted oldest to most recent response)
    """

    # Redirects by default
    r = requests.get('http://github.com')  # default Requests allow redirect
    print(r.url)  # https://github.com/
    print(r.status_code)  # 200
    print(r.history)  # [<Response [301]>]  # Shows history of a redirect

    # Don't allow redirect
    r = requests.get('http://github.com', allow_redirects=False)
    print(r.status_code)  # 301
    print(r.history)  # []


def creating_sessions():
    """
        Session objects let you to persist certain parameters across requests.
        It also persists cookies across all requests made from the Session
        instance
    """
    s = requests.Session()

    # Sessions let cookies persist across requests
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)  # {"cookies": {"sessioncookie": 123456789}}

    # Sessions can also provide default data to the request methods
    # through providing data to the properties on a Session object
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})
    # both 'x-test' and 'x-test2' are sent
    s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
    print(s)


if __name__ == '__main__':
    print('###########################################')
    print('[1] ######### GET WEB PAG DETAILS #########')
    get_webpage_details('https://api.github.com/events')
    print('###########################################')
    print('[2] ######### QUEST API CALLS #########')
    request_API_calls()
    print('###########################################')
    print('[3] ######### PASS PARAMS IN REQUEST #########')
    pass_params_in_urls()
    print('###########################################')
    print('[4] ######### POST FORM DATA REQUEST#########')
    post_form_data_request()
    print('###########################################')
    print('[5] ######### PASS HEADERS IN REQUEST #########')
    pass_headers_in_request()
    print('###########################################')
    print('[5] ######### GET RESPONSE CONTENT #########')
    response_content()
    print('###########################################')
    print('[6] ######### GET JSON RESPONSE CONTENT #########')
    json_response_content()
    print('###########################################')
    print('[9] ######### REQUEST WITH NO REDIRECT #########')
    request_no_redirect()
    print('###########################################')
    print('[10] ######### CREATE REQUEST SESSIONS #########')
    creating_sessions()
