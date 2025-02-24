from pages.base_page import BasePage

class HomePage(BasePage):

    cookies_decline_all = ("xpath", "//*[text() = 'Decline All']")
    home_page_visibility = ("id", "home_logo_reel")
    company_button = ("xpath", '//*[@id="navbarDropdownMenuLink" and contains(text(), "Company")]')
    careers_button = ("xpath", '//a[@href="https://useinsider.com/careers/"]')

    def __init__(self, driver):
        self.driver = driver

    def decline_cookies(self):
        self.click_element(self.cookies_decline_all)
        
    def check_home_page_visibility(self):
        self.wait_for_element(self.home_page_visibility, timeout=20)
    
    def click_company_button(self):
        self.click_element(self.company_button)

    def click_careers_button(self):
        self.click_element(self.careers_button)