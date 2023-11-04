from behave import given
from utils.request_manager import RequestManager
import config

@given('the user makes a simple request')
def step(context):
    context.request_manager = RequestManager(config.BASE_URL, config.COMMON_HEADERS)
    context.response = context.request_manager.send_get_request(config.PRUEBAS)
    print(context.response.json()['data'][0]["perfiles"])