from selenium.webdriver.common.by import By

from utilities.baseclass import Baseclass


class Login_landing(Baseclass):
    image_CSS = "img[class *='thumbnail']"

    def __init__(self, driver):
        self.driver = driver

    def get_title_login_landing_page(self):
        self.wait_for_element(self.driver, Login_landing.image_CSS)
        return self.driver.title
