# from tests.python.features.steps.basic_actions import clean_all_keychain
from config import *


# def before_all(context):
#     set_7p(False)
#     set_6sp(False)


# def before_scenario(context, scenario):


def after_scenario(context, scenario):
    set_7p(True)
    set_6sp(True)

# def after_step(context, step):


# def after_all(context):
#     clean_all_keychain()
