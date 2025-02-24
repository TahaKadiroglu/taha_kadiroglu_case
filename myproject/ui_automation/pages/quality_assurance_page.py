from pages.base_page import BasePage

class QualityAssurancePage(BasePage):

    see_all_qa_jobs_button = ("xpath", "//*[text() = 'See all QA jobs']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_qa_jobs_page(self):
        self.open_url("https://useinsider.com/careers/quality-assurance/")

    def click_all_qa_jobs_button(self):
        self.click_element(self.see_all_qa_jobs_button)