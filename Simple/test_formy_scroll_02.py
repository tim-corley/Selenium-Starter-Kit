from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
from time import sleep
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestScroll():
    @pytest.fixture()
    def chrome_test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=driver_path+'chromedriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://formy-project.herokuapp.com/')
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    @pytest.fixture()
    def firefox_test_setup(self):
        global driver
        driver = webdriver.Firefox(executable_path=driver_path+'geckodriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://formy-project.herokuapp.com/')
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_scroll_chrome(self, chrome_test_setup):
        driver.find_element_by_link_text('Page Scroll').click()
        name_field = driver.find_element_by_id('name')
        actions = ActionChains(driver)
        actions.move_to_element(name_field)
        name_field.send_keys('J. Test')
        sleep(2)

    def test_scroll_firefox(self, firefox_test_setup):
        driver.find_element_by_link_text('Page Scroll').click()
        name_field = driver.find_element_by_id('name')
        actions = ActionChains(driver)
        actions.move_to_element(name_field)
        name_field.send_keys('J. Test')
        sleep(2)
