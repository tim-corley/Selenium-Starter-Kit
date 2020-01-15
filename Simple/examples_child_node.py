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

    def test_child(self, test_setup):
        # <a id="child" href="/child">Child</a></div>
        element = driver.find_element_by_css_selector('div#parent a')
        element.click()
        sleep(1)

    def test_nth_child(self, test_setup):
        # <ul id="list"><li>One</li><li>Two</li><li>Three</li></ul>
        element = driver.find_element_by_css_selector('#list li:nth-child(n)')
        element.click()
        sleep(1)
