from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pytest
import os

global driver_path
parent_path = str(Path(os.getcwd()).parent)
driver_path = parent_path + '/Drivers/'

class TestAutocompleteChrome():
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

    def test_autocomplete(self, test_setup):
        driver.find_element_by_link_text('Autocomplete').click()
        autocomplete = driver.find_element_by_id('autocomplete')
        text = '100 Legends Way, Bos'
        # autocomplete.send_keys('100 Legends Way, Bos') <- this does not trigger autocomplete
        autocomplete.click()
        for character in text:
          actions = ActionChains(driver)
          actions.send_keys(character)
          actions.perform()
        automcomplete_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pac-item')))
        automcomplete_result.click()

class TestAutocompleteFirefox():
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

    def test_autocomplete(self, test_setup):
        driver.find_element_by_link_text('Autocomplete').click()
        autocomplete = driver.find_element_by_id('autocomplete')
        text = '100 Legends Way, Bos'
        autocomplete.click()
        for character in text:
          actions = ActionChains(driver)
          actions.send_keys(character)
          actions.perform()
        automcomplete_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pac-item')))
        automcomplete_result.click()
