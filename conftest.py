import pytest

from selenium import webdriver

# from . import consts


@pytest.fixture(autouse=True, scope="class")
def get_driver(request):
    '''Get Chrome webdriver'''
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
