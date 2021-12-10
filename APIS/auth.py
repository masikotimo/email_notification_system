from wialon import WialonError, Wialon
import json
import requests


def login(wialon_api, token):

    try:
        result = wialon_api.token_login(
            token=token)

        wialon_api.sid = result['eid']
        # print(result['eid'])

        print('Login successfully')
        return result['user']['crt']

    except WialonError as e:
        print(e)


def logout(sid):

    url = 'https://hst-api.wialon.com/wialon/ajax.html?svc=core/logout&params={}&sid={sid}'

    try:
        request = requests.post(url)
        print(request)
        print('Logout successfully')

    except WialonError as e:
        print(e)


token = 'f0611136a2f64d810b638dd8ee6501ab1CAB947ADCE151C574FF1A5AC7DBF90BC06DCD79'


wialon_api = Wialon()
creator_id = login(wialon_api, token)
params = {'creatorId': creator_id, 'name': 'ips_unitttss',
          'hwTypeId': 96266, 'dataFlags': 1}
action_name = 'core/create_unit'


def create_unit():
    try:
        wialon_api.update_extra_params(params)
        print('default params', wialon_api.__default_params)

        wialon_api.call(action_name)
        print("sucessfully")

    except WialonError as e:
        print(e)


create_unit()
