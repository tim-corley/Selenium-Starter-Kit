from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
from time import sleep
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestRadioButtonsChrome():
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

    def test_radio_btn(self, test_setup):
        driver.find_element_by_link_text('Radio Button').click()
        radio_btn_1 = driver.find_element_by_id('radio-button-1')
        radio_btn_1.click()
        sleep(1)
        radio_btn_2 = driver.find_element_by_css_selector('input[value="option2"]')
        radio_btn_2.click()
        sleep(1)
        radio_btn_3 = driver.find_element_by_xpath('html/body/div/div[3]/input')
        radio_btn_3.click()
        sleep(1)

class TestRadioButtonsFirefox():
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

    def test_radio_btn(self, test_setup):
        driver.find_element_by_link_text('Radio Button').click()
        radio_btn_1 = driver.find_element_by_id('radio-button-1')
        radio_btn_1.click()
        sleep(1)
        radio_btn_2 = driver.find_element_by_css_selector('input[value="option2"]')
        radio_btn_2.click()
        sleep(1)
        radio_btn_3 = driver.find_element_by_xpath('html/body/div/div[3]/input')
        radio_btn_3.click()
        sleep(1)
