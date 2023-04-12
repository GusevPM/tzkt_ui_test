from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from time import sleep

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# # enable browser logging
# d = DesiredCapabilities.CHROME
# d['loggingPrefs'] = { 'browser':'ALL' }
# driver = webdriver.Chrome(desired_capabilities=d, options=options)
driver = webdriver.Chrome()

# load the desired webpage
driver.get('https://ghostnet.tzkt.io/')
# WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, './/span[text()=" 0.00000000 "]')))
# print messages
# print(11, len(driver.get_log('browser')))
sleep(2)
if len(driver.get_log('browser')) > 0:
    print(123, 123)

# for entry in driver.get_log('browser'):
#     print(entry)

driver.quit()
