from wialon import Wialon, WialonError
import json
import requests

wialon_api = Wialon()
token = 'f0611136a2f64d810b638dd8ee6501ab1CAB947ADCE151C574FF1A5AC7DBF90BC06DCD79'


def login():

    try:
        result = wialon_api.token_login(
            token=token)

        wialon_api.sid = result['eid']
        # print(result['eid'])

        print('Login successfully')

        wialon_api.core_logout()
    except WialonError as e:
        print(e)


def logout():

    url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/logout&params={}&sid={wialon_api.sid}'

    try:
        request = requests.post(url)
        print(request)
        print('Logout successfully')

    except WialonError as e:
        print(e)


login()
logout()
