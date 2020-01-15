from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from time import sleep
import datetime
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestDropdownChrome():
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

    def test_dropdown_picker(self, test_setup):
        driver.find_element_by_link_text('Dropdown').click()
        dropdown_menu = driver.find_element_by_id('dropdownMenuButton')
        dropdown_menu.click()
        autocomplete_item = driver.find_element_by_id('autocomplete')
        autocomplete_item.click()
        sleep(1)

class TestDropdownFirefox():
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

    def test_dropdown_picker(self, test_setup):
        driver.find_element_by_link_text('Dropdown').click()
        dropdown_menu = driver.find_element_by_id('dropdownMenuButton')
        dropdown_menu.click()
        autocomplete_item = driver.find_element_by_id('autocomplete')
        autocomplete_item.click()
        sleep(1)
