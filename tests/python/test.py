from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.find_element_by_css_selector('test')

driver.execute_script("")
# driver.get("http://somedomain/url_that_delays_loading")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.alert_is_p
#     )
# finally:
#     driver.quit()
