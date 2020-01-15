# must be within Tests folder to run
# Complete/Tests $ pytest -v
import sys
sys.path.append('..')
from Pages.page_form import FormPage
from globals import FormyGlobals
from selenium import webdriver
import pytest

class TestFormSuccessChrome():
    @pytest.fixture()
    def test_setup(self):
        global driver
        path = str(FormyGlobals.chrome_driver_path)
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(FormyGlobals.form_url)
        yield
        driver.close()
        driver.quit()
        print('\nTest Completed\n')

    def test_complete_form_success(self, test_setup):
        form = FormPage(driver)
        form.complete_form(FormyGlobals.first_name, FormyGlobals.last_name, FormyGlobals.job_title, FormyGlobals.date_string)
        form.submit_form()
        assert 'The form was successfully submitted!' == form.success_result()

class TestFormSuccessFirefox():
    @pytest.fixture()
    def test_setup(self):
        global driver
        path = str(FormyGlobals.gecko_driver_path)
        driver = webdriver.Firefox(executable_path=path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(FormyGlobals.form_url)
        yield
        driver.close()
        driver.quit()
        print('\nTest Completed\n')

    def test_complete_form_success(self, test_setup):
        form = FormPage(driver)
        form.complete_form(FormyGlobals.first_name, FormyGlobals.last_name, FormyGlobals.job_title, FormyGlobals.date_string)
        form.submit_form()
        assert 'The form was successfully submitted!' == form.success_result()
