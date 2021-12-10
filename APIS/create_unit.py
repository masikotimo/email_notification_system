from .auth import login
from . import token
from wialon import Wialon, WialonError

token = token.token

wialon_api = Wialon()
creator_id = login(wialon_api, token)
params = {'creatorId': creator_id, 'name': 'ips_unitttss',
          'hwTypeId': 96266, 'dataFlags': 1}
action_name = 'core/create_unit'


def create_unit():
    wialon_api.__default_params = params
    wialon_api.call(action_name)


create_unit()
