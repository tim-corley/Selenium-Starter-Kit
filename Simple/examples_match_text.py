from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
from time import sleep
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestTextMatchChrome():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=driver_path+'chromedriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://formy-project.herokuapp.com/')
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_by_prefix(self, test_setup):
        # <div id="randomId_textField">
        element = driver.find_element_by_css_selector('div[id^="textField"]')
        element.click()
        sleep(1)

    def test_by_substring(self, test_setup):
        # <div id="123_textField_randomId">
        element = driver.find_element_by_css_selector('div[id*="textField"]')
        element.click()
        sleep(1)

    def test_by_suffix(self, test_setup):
        # <div id="randomId_textField">
        element = driver.find_element_by_css_selector('div[id="textField"]')
        element.click()
        sleep(1)

    def test_by_exact(self, test_setup):
        # <div id="textField">
        element = driver.find_element_by_css_selector('div[id="textField"]')
        element.click()
        sleep(1)
