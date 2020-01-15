from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path
from time import sleep
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestDragDropChrome():
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

    def test_drag_drop(self, test_setup):
        driver.find_element_by_link_text('Drag and Drop').click()
        image = driver.find_element_by_id('image')
        box = driver.find_element_by_id('box')
        actions = ActionChains(driver)
        actions.drag_and_drop(image, box).perform()
        sleep(1)


class TestDragDropFirefox():
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

    def test_drag_drop(self, test_setup):
        driver.find_element_by_link_text('Drag and Drop').click()
        image = driver.find_element_by_id('image')
        box = driver.find_element_by_id('box')
        actions = ActionChains(driver)
        actions.drag_and_drop(image, box).perform()
        sleep(1)
