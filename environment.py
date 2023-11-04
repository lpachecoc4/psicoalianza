from behave import fixture, use_fixture
from utils.request_manager import RequestManager
from config import BASE_URL

# Define a fixture for environment setup and teardown
@fixture
def setup_teardown(context):
    # Set up the test environment before running scenarios
    context.request_manager = RequestManager(base_url=BASE_URL)
    
    # You can perform other setup tasks here if needed
    
    yield context  # The control is yielded back to run the scenarios
    
    # Tear down the test environment after running scenarios
    context.request_manager.close()  # Close any resources like HTTP sessions

# Register the fixture with Behave
def before_all(context):
    use_fixture(setup_teardown, context)

# Optionally, you can define additional hooks for more specific tasks:
# def before_scenario(context, scenario):
# def after_scenario(context, scenario):
# def before_feature(context, feature):
# def after_feature(context, feature)
# ...

# Define other configuration or utility functions as needed

