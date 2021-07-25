import time

from selenium.webdriver.common.by import By

from page_objects.login_page import Login_page
from utilities.baseclass import Baseclass


class Homepage(Baseclass):
    login_acct_button = (By.CSS_SELECTOR, "div[class*='-login'] a")
    login_link = (By.LINK_TEXT, "Login")
    company_dropdown_values = (By.XPATH, "//div[@id='mobileMenuMain']/nav/ul[2]/li/ul/li")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def goto_login_page(self):
        self.driver.find_element(*Homepage.login_acct_button).click()
        self.driver.find_element(*Homepage.login_link).click()
        login_page = Login_page(self.driver)
        return login_page

    def goto_home(self):
        self.driver.get("https://www.phptravels.net/home")
        self.wait_for_element(self.driver, "div[class*='-login'] a")

    def close_browser(self):
        self.driver.close()

    def select_company_dropdown(self):
        self.select_by_link_text(self.driver, "COMPANY")
        self.wait_for_element_xpath(self.driver, *Homepage.company_dropdown_values)
        dropdown_elements = self.driver.find_elements(*Homepage.company_dropdown_values)
        dropdown_values = []
        for item in dropdown_elements:
            dropdown_values.append(item.find_element_by_xpath("a").text)

        return dropdown_values
