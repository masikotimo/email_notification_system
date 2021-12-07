from wialon import Wialon, WialonError
import json

try:
    wialon_api = Wialon()
    # old username and password login is deprecated, use token login
    token = 'f0611136a2f64d810b638dd8ee6501ab1CAB947ADCE151C574FF1A5AC7DBF90BC06DCD79'
    result = wialon_api.token_login(
        token=token)

    wialon_api.sid = result['eid']
    # creator_id = result['user']['crt']

    # params = {'creatorId': creator_id, 'name': 'ips_unitttss',
    #           'hwTypeId': 96266, 'dataFlags': 1}

    # action_name = 'svc=core/create_unit'
    # url = 'https://hst-api.wialon.com/wialon/ajax.html'
    # # params = {
    # #         'svc': action_name.replace('_', '/', 1),
    # #         'params': params.encode('utf-8'),
    # #         'sid': sid
    # #     }

    # res = wialon_api.request(action_name, url, params)

    # resultx = wialon_api.avl_evts()

    # print(json.dumps(result))
    print(result)

    wialon_api.core_logout()
except WialonError as e:
    print(e)
