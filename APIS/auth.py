from wialon import WialonError, Wialon
import json
import requests


def login(wialon_api, token):

    try:
        result = wialon_api.token_login(
            token=token)

        wialon_api.sid = result['eid']
        print(result['eid'])

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

create_user_params = {"id": 352093083080803,
                      "flags": 4}
action_name = 'core/create_unit'
create_user_action_name = 'core/search_item'


def create_unit():
    try:
        print(wialon_api.avl_evts())

        wialon_api.call(create_user_action_name, **create_user_params)
        print("sucessfully")

    except WialonError as e:
        print(e)


# when login suceed then run init() function
#  load items to current session
#  Items specification
#  exit if error code
#  get loaded 'avl_unit's items
#  check if units found
view_units_params = {
    "spec": [{"type": "type", "data": "avl_resource", "flags": 1, "mode": 0}]}

svc = "core/update_data_flags"


# host?svc=core/update_data_flags&params={"spec":[{"type":"type","data":"avl_unit","flags":1,"mode":0}]}&sid=09f13de5c5074c0ce972384d48908e21


def view_units():
    try:

        result = wialon_api.call(svc, **view_units_params)
        resId = (result[0]["i"])
        view_units_paramsx = {
            "spec": [{"type": "id", "data": resId, "flags": 1, "mode": 0}]}
        result = wialon_api.call(svc, **view_units_paramsx)
        print(result)

    except WialonError as e:
        print(e)


view_units()
