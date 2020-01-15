from selenium import webdriver
from pathlib import Path
from time import sleep
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestModalChrome():
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

    def test_modal_click(self, test_setup):
        driver.find_element_by_link_text('Modal').click()
        modal_btn = driver.find_element_by_id('modal-button')
        modal_btn.click()
        sleep(1)
        close_btn = driver.find_element_by_id('close-button')
        driver.execute_script('arguments[0].click()', close_btn)
        sleep(1)

class TestModalFirefox():
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

    def test_modal_click(self, test_setup):
        driver.find_element_by_link_text('Modal').click()
        modal_btn = driver.find_element_by_id('modal-button')
        modal_btn.click()
        sleep(1)
        close_btn = driver.find_element_by_id('close-button')
        driver.execute_script('arguments[0].click()', close_btn)
        sleep(1)
