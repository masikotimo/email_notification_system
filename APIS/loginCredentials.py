from wialon import Wialon, WialonError
import json

try:
    wialon_api = Wialon()
    # old username and password login is deprecated, use token login
    result = wialon_api.token_login(token='c8087c7e1c7f66a25d38b1ecd9dfe33a6A997C8F1C5CC03CBF1FF8B4A4F09136ACF0B0CE')
    wialon_api.sid = result['eid']

    resultx = wialon_api.avl_evts()

    print (json.dumps(result))
    # print (resultx)

    wialon_api.core_logout()
except WialonError as e:
    pass