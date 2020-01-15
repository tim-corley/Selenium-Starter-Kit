from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import datetime
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestCompleteFormChrome():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=driver_path+'chromedriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://formy-project.herokuapp.com/form')
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_complete_form(self, test_setup):
        driver.find_element_by_id('first-name').send_keys('Quality')
        driver.find_element_by_id('last-name').send_keys('Tester')
        driver.find_element_by_id('job-title').send_keys('QA Engineer')
        driver.find_element_by_id('radio-button-2').click()
        driver.find_element_by_id('checkbox-1').click()
        driver.find_element_by_css_selector('option[value="2"]').click()
        date_field = driver.find_element_by_id('datepicker')
        date_field.click()
        date_string = datetime.datetime.now().strftime('%m/%d/%Y')
        date_field.send_keys(date_string)
        date_field.send_keys(Keys.RETURN)
        driver.find_element_by_css_selector('.btn.btn-lg.btn-primary').click()
        success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'alert')))
        assert success.text == 'The form was successfully submitted!'

class TestCompleteFormFirefox():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Firefox(executable_path=driver_path+'geckodriver')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://formy-project.herokuapp.com/form')
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_complete_form(self, test_setup):
        driver.find_element_by_id('first-name').send_keys('Quality')
        driver.find_element_by_id('last-name').send_keys('Tester')
        driver.find_element_by_id('job-title').send_keys('QA Engineer')
        driver.find_element_by_id('radio-button-2').click()
        driver.find_element_by_id('checkbox-1').click()
        driver.find_element_by_css_selector('option[value="2"]').click()
        date_field = driver.find_element_by_id('datepicker')
        date_field.click()
        date_string = datetime.datetime.now().strftime('%m/%d/%Y')
        date_field.send_keys(date_string)
        date_field.send_keys(Keys.RETURN)
        driver.find_element_by_css_selector('.btn.btn-lg.btn-primary').click()
        success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'alert')))
        assert success.text == 'The form was successfully submitted!'
