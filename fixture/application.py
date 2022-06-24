from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.ie.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url, base_password):
        if browser == "firefox":
            self.wd = WebDriver()
        elif browser == "chrome":
            self.wd = WebDriver()
        elif browser == "ie":
            self.wd = WebDriver()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.base_password = base_password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
