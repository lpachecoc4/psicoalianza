from behave import fixture, use_fixture
from utils.request_manager import RequestManager
from config import BASE_URL, COMMON_HEADERS


@fixture
def setup_teardown(context):
    context.request_manager = RequestManager(BASE_URL, COMMON_HEADERS)
    yield context
    context.request_manager.close()

def before_all(context):
    use_fixture(setup_teardown, context)

@fixture
def setup_data(context):
    context.data = {}
    context.pruebas = []
    yield context
    context.data = {}
    context.pruebas = []

def before_scenario(context, scenario):
    use_fixture(setup_data, context)


