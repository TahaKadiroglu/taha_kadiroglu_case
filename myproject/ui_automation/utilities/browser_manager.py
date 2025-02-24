from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class BrowserManager:

    def get_driver(browser="chrome"):
        if browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-cookies")
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=chrome_options)
        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.set_preference("dom.disable_beforeunload", True)
            firefox_options.set_preference("privacy.popups.showBrowserMessage", False)
            firefox_options.set_preference("network.cookie.cookieBehavior", 2)
            firefox_options.set_preference("privacy.firstparty.isolate", True)
            firefox_options.set_preference("profile.default_content_settings.cookies", 2)
            driver = webdriver.Firefox(options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser is selected: {browser}")

        driver.maximize_window()
        return driver

    def quit_driver(driver):
        driver.quit()