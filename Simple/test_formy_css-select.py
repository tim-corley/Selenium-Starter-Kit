from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
from time import sleep
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestCssSelectChrome():
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

    def test_css_selector(self, test_setup):
        driver.find_element_by_link_text('Buttons').click()
        dropdown_btn = driver.find_element_by_css_selector('button[class="btn btn-lg btn-primary dropdown-toggle"]')
        dropdown_btn.click()
        sleep(1)


class TestCssSelectFirefox():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Firefox(executable_path=driver_path+'geckodriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://formy-project.herokuapp.com/')
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_css_selector(self, test_setup):
        driver.find_element_by_link_text('Buttons').click()
        dropdown_btn = driver.find_element_by_css_selector('button[class="btn btn-lg btn-primary dropdown-toggle"]')
        dropdown_btn.click()
        sleep(1)
