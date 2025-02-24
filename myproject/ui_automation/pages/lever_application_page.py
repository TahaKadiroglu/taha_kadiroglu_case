from pages.base_page import BasePage

class LeverApplicationPage(BasePage):

    job_description = ("xpath", "//*[@data-qa = 'job-description']")
    apply_for_this_job_button = ("xpath", "//*[text()= 'Apply for this job']")

    def __init__(self, driver):
        self.driver = driver

    def check_lever_application_page_visibility(self):
        self.wait_for_element(self.job_description)