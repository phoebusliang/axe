import os
from behave import *
from selenium.webdriver import ActionChains
import startkit.steps.basic_actions as bo
import requests
import json


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
    user_playload = {}


@step('Clear username and password')
def clear_user_info(context):
    response = requests.post(context.url + '/' + context.session + '/element/user_ele_id/clear')
    assert (response.status_code == 200)


@step('Click the "Detail Pane Collapser" and make it be "{expanded_or_collapsed}"')
def click_the_collapser(context, expanded_or_collapsed):
    context.browser.find_element_by_css_selector('.detail-pane-collapser').click()


@step('"{enlarge_or_shrink}" the "Instrument Detail Pane" with {offset} pixel')
def drag_instrument_detail_pane(context, enlarge_or_shrink, offset):
    action_chain = ActionChains(context.browser)
    dragger = bo.wait_for_script(context.browser, "return $('.detail-pane-dragger i')[0]",
                                 check=lambda element: element)
    action_chain.click_and_hold(dragger).move_by_offset(0, int(
        offset)).release().perform() if enlarge_or_shrink == 'enlarge' else action_chain.click_and_hold(
        dragger).move_by_offset(0, -int(offset)).release().perform()
    action_chain.click_and_hold(dragger).click().move_by_offset(0, 200).click(dragger).release().perform()
