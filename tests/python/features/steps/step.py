import json

import requests
from behave import *

# import tests.python.features.steps.basic_actions as bo
import basic_actions as bo


@given('Open the pv page with client: "{client}" Date: "{date}" and fund: "{fund}"')
def open_pv_page(context, client, date, fund):
    context.browser.get('http://localhost:3000/' + client + '/' + date + '?' + fund)


@given('Start the app on "{device}"')
def launch_app(context, device):
    options = {
        "7p": "http://localhost:8101/session",
        "6sp": "http://localhost:8102/session"
    }
    payload = {"desiredCapabilities": {"bundleId": "com.thoughtworks.StartKit"}}
    response = requests.post(options.get(device), data=json.dumps(payload))
    context.url = options.get(device)
    context.session = json.loads(response.text)['sessionId']


@step('Input the username: "{user}" and password: "{psw}"')
def input_user_info(context, user, psw):
    body_user = {'value': user}
    context.route = context.url + '/' + context.session + '/element/' + context.user_id + '/value'
    res = bo.wait_for_element(context, 'post', body_user, check=lambda data: context.user_id in data)

    context.route = context.url + '/' + context.session + "/elements"
    body_psw_field = {"using": "class name", "value": "XCUIElementTypeSecureTextField"}
    res = bo.wait_for_element(context, 'post', body_psw_field,
                              check=lambda data: 'XCUIElementTypeSecureTextField' in data)
    context.psw_id = json.loads(res)['value'][0]['ELEMENT']

    body_psw_val = {'value': psw}
    context.route = context.url + '/' + context.session + '/element/' + json.loads(res)['value'][0][
        'ELEMENT'] + '/value'
    res = bo.wait_for_element(context, 'post', body_psw_val, check=lambda data: json.loads(res)['value'][0][
                                                                                    'ELEMENT'] in data)


@step('Tap "Login"')
def input_user_info(context):
    context.route = context.url + '/' + context.session + "/elements"
    body_login_loc = {"using": "class name", "value": "XCUIElementTypeButton"}
    res = bo.wait_for_element(context, 'post', body_login_loc, check=lambda data: 'Login' in data)

    for item in json.loads(res)['value']:
        if item['label'] == 'Login':
            context.login = item['ELEMENT']
            break
    context.route = context.url + '/' + context.session + '/element/' + context.login + '/click'
    bo.wait_for_element(context, 'post', check=lambda data: context.login in data)


@step('Clear username and password')
def clear_user_info(context):
    context.route = context.url + '/' + context.session + "/elements"
    body = {"using": "class name", "value": "XCUIElementTypeTextField"}
    res = bo.wait_for_element(context, "post", body, check=lambda data: "XCUIElementTypeTextField" in data)
    res_json = json.loads(res)
    context.user_id = res_json['value'][0]['ELEMENT']
    context.route = context.url + '/' + context.session + '/element/' + res_json['value'][0]['ELEMENT'] + '/clear'
    response = bo.wait_for_element(context, "post", body, check=lambda data: res_json['value'][0]['ELEMENT'] in data)
    assert (json.loads(response)['status'] == 0)


@step('Setup the environment for "{device}"')
def setup_env(context, device):
    bo.clean_env(device)
