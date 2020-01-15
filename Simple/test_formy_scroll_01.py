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

class TestScrollChrome():
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

    def test_scroll(self, test_setup):
        driver.find_element_by_link_text('Page Scroll').click()
        name_field = driver.find_element_by_id('name')
        actions = ActionChains(driver)
        actions.move_to_element(name_field)
        name_field.send_keys('J. Test')
        sleep(1)
        date = driver.find_element_by_id('date')
        date_string = datetime.datetime.now().strftime('%m/%d/%Y')
        date.send_keys(date_string)
        sleep(1)


class TestScrollFirefox():
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

    def test_scroll(self, test_setup):
        driver.find_element_by_link_text('Page Scroll').click()
        name_field = driver.find_element_by_id('name')
        actions = ActionChains(driver)
        actions.move_to_element(name_field)
        name_field.send_keys('J. Test')
        sleep(1)
        date = driver.find_element_by_id('date')
        date_string = datetime.datetime.now().strftime('%m/%d/%Y')
        date.send_keys(date_string)
        sleep(1)
