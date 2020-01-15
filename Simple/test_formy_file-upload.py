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

class TestFileUploadChrome():
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

    def test_file_upload(self, test_setup):
        file_name = '_100.jpg'
        driver.find_element_by_link_text('File Upload').click()
        file_upload_field = driver.find_element_by_id('file-upload-field')
        file_upload_field.send_keys(file_name)
        sleep(1)

class TestFileUploadFirefox():
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

    def test_file_upload(self, test_setup):
        file_name = '_100.jpg'
        driver.find_element_by_link_text('File Upload').click()
        file_upload_field = driver.find_element_by_id('file-upload-field')
        file_upload_field.send_keys(file_name)
        sleep(1)
