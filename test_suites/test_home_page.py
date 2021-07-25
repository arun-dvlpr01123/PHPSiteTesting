import time

import pytest
from selenium import webdriver

from page_objects.home_page import Homepage
from utilities.baseclass import Baseclass


class Test_Homepage_Login_with_valid_cred(Baseclass):

    def test_landing_page(self):
        home_page = Homepage(self.driver)
        site_title = home_page.get_title()
        assert site_title == "PHPTRAVELS | Travel Technology Partner", "Title Mismatch"

    def test_login_page_valid_cred(self):
        home_page = Homepage(self.driver)
        login_page = home_page.goto_login_page()
        login_landing_page = login_page.login_with_valid_cred()
        site_title = login_landing_page.get_title_login_landing_page()
        assert site_title == "My Account", "Title Mismatch"
        home_page.close_browser()


class Test_Homepage_Login_with_invalid_cred(Baseclass):
    def test_login_page_invalid_cred(self):
        home_page = Homepage(self.driver)

        home_page.goto_home()
        login_page = home_page.goto_login_page()
        self.cred = login_page.login_with_invalid_cred()
        error_message = self.cred
        assert error_message != "Invalid credentials message missing", "Test case failed "
        assert error_message == "Invalid Email or Password"

        # self.driver.find_element_by_css_selector("div[class*='-login'] a").click()
        # self.driver.find_element_by_link_text("Login").click()
        # site_title = self.driver.title
        # assert site_title == "Login", "Title Mismatch"
        # self.driver.find_element_by_css_selector("input[name='username']").send_keys("user@phptravels.com")
        # self.driver.find_element_by_css_selector("input[name='password']").send_keys("demouser")
        # self.driver.find_element_by_css_selector("button[class*='loginbtn']").click()
        # self.wait_for_element(self.driver,"img[class *='thumbnail']")
        # site_title = self.driver.title
        # assert site_title == "My Account", "Title Mismatch"
