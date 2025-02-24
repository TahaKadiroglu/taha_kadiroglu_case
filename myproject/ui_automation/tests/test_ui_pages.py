import unittest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.quality_assurance_page import QualityAssurancePage
from pages.open_positions_page import OpenPositionsPage
from pages.lever_application_page import LeverApplicationPage
from pages.base_page import BasePage
from utilities.browser_manager import BrowserManager
import time

class test_insider(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserManager.get_driver(browser="chrome")
        cls.driver.get("https://useinsider.com/")
        cls.home_page = HomePage(cls.driver)
        cls.base_page = BasePage(cls.driver)

    def tearDown(self):
        if hasattr(self, '_outcome'):
            result = self._outcome.result
            if result.errors or result.failures:
                test_name = self._testMethodName
                self.base_page.take_screenshot(test_name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test1_home_page_visibility(self):
        self.home_page.decline_cookies()
        self.home_page.check_home_page_visibility()

    def test2_company_menu_and_check_career_page(self):
        self.home_page.click_company_button()
        self.home_page.click_careers_button()
        self.careers_page = CareersPage(self.driver)
        self.careers_page.our_locations_visibility()
        self.careers_page.teams_area_visibility()
        self.careers_page.life_at_insider_visibility()

    def test3_filter_qa_jobs_check_details_of_roles_click_view_role(self):
        self.quality_assurance_page = QualityAssurancePage(self.driver)
        self.quality_assurance_page.go_to_qa_jobs_page()
        self.quality_assurance_page.click_all_qa_jobs_button()
        self.open_positions_page = OpenPositionsPage(self.driver)
        self.open_positions_page.wait_for_qa_department_filter()
        time.sleep(1)
        self.open_positions_page.click_filter_by_location()
        self.open_positions_page.select_istanbul_turkiye()
        self.open_positions_page.wait_for_presence_of_qa_jobs()
        self.open_positions_page.check_job_posts_content()
        self.open_positions_page.click_first_view_role_button()

    def test4_check_lever_application_page(self):
        self.lever_app_page = LeverApplicationPage(self.driver)
        self.lever_app_page.switch_new_window()
        self.lever_app_page.check_lever_application_page_visibility()

if __name__ == "__main__":
    unittest.main()