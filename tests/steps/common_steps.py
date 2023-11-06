from behave import given, when, then, step
from assertpy import assert_that, soft_assertions
import config


@given("the user has the following data")
def step_implementation(context):
    for row in context.table:
        if(row["value"] == "true" or row["value"] == "false"):
            context.data[row["key"]] = bool(row["value"])
        else:
            context.data[row["key"]] = row["value"]

@given("the user adds the following prueba")
def step_implementation(context):
    prueba = {}
    for row in context.table:
        prueba[row["key"]] = int(row["value"])
    context.pruebas.append(prueba)
    context.data["pruebas"] = context.pruebas

@when("the user sends a POST request to create a proceso")
def step_implementation(context):
    context.response = context.request_manager.send_post_request(config.PROCESOS, json=context.data)

@then("the response status code should be '{status_code}'")
def step_implementation(context, status_code):
    assert context.response.status_code == int(status_code)

@then("the error message should be '{text}'")
def step_implementation(context, text):
    assert context.response.json()["error"]["proceso_nombre"][0] == text
    
@then("the error should be '{text}'")
def step_implementation(context, text):
    assert context.response.json()["error"] == text

@step("the response data should have")
def step_implementation(context):
    data = {}
    for row in context.table:
        if(row["value"] == "true" or row["value"] == "false"):
            data[row["key"]] = bool(row["value"])
        else:
            data[row["key"]] = row["value"]
    with soft_assertions():
        assert_that(data).is_subset_of(context.response.json()["data"])

@then("the pruebas should have")
def step_implementation(context):
    data = {}
    for row in context.table:
        data[row["key"]] = int(row["value"])
    with soft_assertions():
        assert_that(data).is_subset_of(context.response.json()["data"]["pruebas"][0])

