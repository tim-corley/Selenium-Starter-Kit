from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
from time import sleep
import datetime
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestSwitchChrome():
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

    def test_window_switch(self, test_setup):
        driver.find_element_by_link_text('Switch Window').click()
        new_tab_btn = driver.find_element_by_id('new-tab-button')
        new_tab_btn.click()
        original_handle = driver.window_handles[0]
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        sleep(1)
        driver.switch_to.window(original_handle)
        sleep(1)

    def test_alert_switch(self, test_setup):
        driver.find_element_by_link_text('Switch Window').click()
        alert_btn = driver.find_element_by_id('alert-button')
        alert_btn.click()
        sleep(1)
        alert = driver.switch_to.alert
        sleep(1)
        alert.accept()
        sleep(1)


class TestSwitchFirefox():
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

    def test_window_switch(self, test_setup):
        driver.find_element_by_link_text('Switch Window').click()
        new_tab_btn = driver.find_element_by_id('new-tab-button')
        new_tab_btn.click()
        original_handle = driver.window_handles[0]
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        sleep(1)
        driver.switch_to.window(original_handle)
        sleep(1)

    def test_alert_switch(self, test_setup):
        driver.find_element_by_link_text('Switch Window').click()
        alert_btn = driver.find_element_by_id('alert-button')
        alert_btn.click()
        sleep(1)
        alert = driver.switch_to.alert
        sleep(1)
        alert.accept()
        sleep(1)
