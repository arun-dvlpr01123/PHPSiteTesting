import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from page_objects.login_landing import Login_landing
from utilities.baseclass import Baseclass


class Login_page(Baseclass):
    email_input_box = (By.CSS_SELECTOR, "input[name='username']")
    password_input_box = (By.CSS_SELECTOR, "input[name='password']")
    login_button = (By.CSS_SELECTOR, "button[class*='loginbtn']")
    invalid_cred_message = (By.CSS_SELECTOR, "div[class*='alert-danger']")

    # self.driver.find_element_by_css_selector("input[name='password']").send_keys("demouser")
    # self.driver.find_element_by_css_selector("button[class*='loginbtn']").click()
    def __init__(self, driver):
        self.driver = driver

    def login_with_valid_cred(self):
        self.driver.find_element(*Login_page.email_input_box).send_keys("user@phptravels.com")
        self.driver.find_element(*Login_page.password_input_box).send_keys("demouser")
        self.driver.find_element(*Login_page.login_button).click()
        login_landing = Login_landing(self.driver)
        return login_landing

    def login_with_invalid_cred(self):
        self.driver.find_element(*Login_page.email_input_box).send_keys("aruncan@outlook.com")
        self.driver.find_element(*Login_page.password_input_box).send_keys("apple")
        self.driver.find_element(*Login_page.login_button).click()
        time.sleep(5)
        try:
            invalid_message = self.driver.find_element(*Login_page.invalid_cred_message)
        except NoSuchElementException:
            return "Invalid credentials message missing"
        return invalid_message.text
