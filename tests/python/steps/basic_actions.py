import json
import time

import requests

options = {
    "7p": "49066C3A-1BB3-440B-B660-C9AAF02B176A",
    "6sp": "BC9D083F-111E-4022-A5BA-EF1BDB9B8AD0",
    "6s": "92A7F012-0270-4C06-83F9-DEF643883CC8",
    "6p": "A915EE37-E942-43D7-8F67-B1ADDC743433"
}

sleep_time = 2

bundle_id = 'com.thoughtworks.StartKit'

app_path = '/Users/twe/Downloads/com.thoughtworks.StartKit'

command_path = '/Users/twe/Documents/fbsimctl/fbsimctl'


def wait_for_element(context, request_type, body='', check=bool, timeout=10, error_template="Value is %s"):
    start = time.time()
    while time.time() - start < timeout:
        if request_type == "post":
            response = requests.post(context.route, data=json.dumps(body))
        else:
            response = requests.get(context.url)
        response = response.text
        print(response)
        if check(response):
            return response
        time.sleep(1)
    raise AssertionError(error_template % response)


def wait_for_script(browser, script, check=bool, timeout=30, error_template="Value is %s"):
    start = time.time()
    while time.time() - start < timeout:
        value = browser.execute_script(script)
        if check(value):
            return value
    raise AssertionError(error_template % value)


def clean_keychain(device):
    requests.get(
        command_path + ' ' + options.get(device) + ' clear_keychain ' + bundle_id)
    time.sleep(2)


def install_app(device):
    requests.get(
        command_path + ' ' + options.get(device) + ' install ' + app_path)
    time.sleep(2)


def uninstall_app(device):
    requests.get(
        command_path + ' ' + options.get(device) + ' uninstall ' + bundle_id)
    time.sleep(2)


def clean_all_keychain():
    requests.get(command_path + ' --state=booted clear_keychain ' + bundle_id)


def clean_env(device):
    clean_keychain(device)
    uninstall_app(device)
    install_app(device)


def clean_all_env():
    clean_all_keychain()