from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from .. import consts
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMainPage():
    # driver = webdriver.Chrome()

    def test_open(self):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = { 'browser':'ALL' }
        driver = webdriver.Chrome(desired_capabilities=d)
        driver.get(consts.BASE_URL)
        for e in driver.get_log('browser'):
            print(1111)
            print(e)
        
        # assert 1 == 1


TestMainPage.test_open()
