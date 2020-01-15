from pathlib import Path
import datetime
import os

class FormyGlobals:
    parent_path = str(Path(os.getcwd()).parent.parent)
    driver_path = parent_path + '/Drivers/'
    chrome_driver_path = driver_path + 'chromedriver'
    gecko_driver_path = driver_path + 'geckodriver'
    form_url = 'https://formy-project.herokuapp.com/form'
    first_name = 'Thomas'
    last_name = 'Tester'
    job_title = 'Software Engineer in Test'
    date_string = datetime.datetime.now().strftime('%m/%d/%Y')
