import sys
sys.path.append('..')
from globals import FormyGlobals
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage():
    # constructor
    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox_id = 'first-name'
        self.last_name_textbox_id = 'last-name'
        self.title_textbox_id = 'job-title'
        self.education_radio_id = 'radio-button-2'
        self.gender_check_id = 'checkbox-1'
        self.experience_select_css = 'option[value="2"]'
        self.datepicker_id = 'datepicker'
        self.submit_button_css = '.btn.btn-lg.btn-primary'
        self.success_alert_css = 'alert'

    def complete_form(self, first_name, last_name, job_title, datetime_data):
        self.driver.find_element_by_id(self.first_name_textbox_id).clear()
        self.driver.find_element_by_id(self.first_name_textbox_id).send_keys(first_name)
        self.driver.find_element_by_id(self.last_name_textbox_id).clear()
        self.driver.find_element_by_id(self.last_name_textbox_id).send_keys(last_name)
        self.driver.find_element_by_id(self.title_textbox_id).clear()
        self.driver.find_element_by_id(self.title_textbox_id).send_keys(job_title)
        self.driver.find_element_by_id(self.education_radio_id).click()
        self.driver.find_element_by_id(self.gender_check_id).click()
        self.driver.find_element_by_css_selector(self.experience_select_css).click()
        self.driver.find_element_by_id(self.datepicker_id).click()
        self.driver.find_element_by_id(self.datepicker_id).send_keys(datetime_data)
        self.driver.find_element_by_id(self.datepicker_id).send_keys(Keys.RETURN)

    def submit_form(self):
        self.driver.find_element_by_css_selector(self.submit_button_css).click()

    def success_result(self):
        success = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, self.success_alert_css)))
        return success.text
