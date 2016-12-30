# from tests.python.features.steps.basic_actions import clean_all_keychain
import os

from config import *
from features.steps.basic_actions import clean_all_keychain
from lock import Lock, locks

# devices = {
#     "7p": "49066C3A-1BB3-440B-B660-C9AAF02B176A",
#     "6sp": "BC9D083F-111E-4022-A5BA-EF1BDB9B8AD0",
#     "6s": "92A7F012-0270-4C06-83F9-DEF643883CC8",
#     "6p": "A915EE37-E942-43D7-8F67-B1ADDC743433"
# }


# def before_all(context):
#     set_7p(False)
#     set_6sp(False)


# def before_scenario(context, scenario):
#     print('*****' + scenario.description)


# def after_scenario(context, scenario):
# lock = Lock("/tmp/" + context.device)
# lock.release()
# locks.get(context.device).release()
# AssertionError("testestestestseetes")


# lock = Lock("/tmp/" + context.device + '.tmp')
# print("ZZZZZZZZZ::" + str(os.getpid()))
# lock.release()


# def after_step(context, step):


# def after_all(context):
#     print("testestestestseetes")
#     clean_all_keychain()
