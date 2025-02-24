import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        
    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def find_element(self, locator):
        self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def switch_new_window(self):
        original_window = self.driver.current_window_handle
        windows = self.driver.window_handles
        for window in windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
    
    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, 500);")    

    def take_screenshot(self, test_name):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshots/{test_name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved: {screenshot_name}")