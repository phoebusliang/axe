import os
import shutil
from selenium import webdriver
from tests.python.steps.basic_actions import clean_env
import requests


# def before_all(context):
# context.browser.set_window_size(1280, 768)
# clean_env()
# folder_opr('data', 'generate')


# def folder_opr(folders, opr):
#     # folder_list = folders.split(',')
#     # if opr == "delete":
#     #     for folder in folder_list:
#     #         if os.path.exists(folder.strip()):
#     #             shutil.rmtree(folder)
#     # else:
#     #     for folder in folder_list:
#     #         if not os.path.exists(folder.strip()):
#     #             os.makedirs(folder)


# def before_scenario(context, scenario):
    # driver_arguments = {'chrome_options': python.ChromeOptions()}
    # prefs = {"download.default_directory": os.path.join(os.getcwd() + os.sep + 'data')}
    # driver_arguments['chrome_options'].add_argument('--no-sandbox')
    # driver_arguments['chrome_options'].add_experimental_option('prefs', prefs)
    # context.browser = python.Chrome(chrome_options=driver_arguments['chrome_options'])
    # context.browser.set_window_size(1280, 768)
    # clean_env()
    # folder_opr('data', 'generate')
    # delete_all_imposters()


# def after_scenario(context, scenario):
    # clean_env()
    # folder_opr('data', 'delete')
    # context.browser.quit()
    # delete_all_imposters()




# def after_step(context, step):
#     if step.status == "failed":
#         if not os.path.exists('screenshots'):
#             os.makedirs('screenshots')
#         context.browser.save_screenshot('screenshots/' + str(step) + '.png')


# def after_all(context):
#     context.browser.quit()
