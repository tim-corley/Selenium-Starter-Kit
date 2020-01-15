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

class TestDatePickerChrome():
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

    def test_date_picker(self, test_setup):
        driver.find_element_by_link_text('Datepicker').click()
        date_field = driver.find_element_by_id('datepicker')
        date_field.click()
        date_string = datetime.datetime.now().strftime('%m/%d/%Y')
        date_field.send_keys(date_string)
        date_field.send_keys(Keys.RETURN)
        sleep(1)

class TestDatePickerFirefox():
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

    def test_date_picker(self, test_setup):
        driver.find_element_by_link_text('Datepicker').click()
        date_field = driver.find_element_by_id('datepicker')
        date_field.click()
        date_string = datetime.datetime.now().strftime('%m/%d/%Y')
        date_field.send_keys(date_string)
        date_field.send_keys(Keys.RETURN)
        sleep(1)
