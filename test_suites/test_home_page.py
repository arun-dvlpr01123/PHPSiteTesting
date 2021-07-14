import time

import pytest
from selenium import webdriver

from utilities.baseclass import Baseclass


class Test_Homepage(Baseclass):

    def test_landing_page(self):
        site_title = self.driver.title
        assert site_title == "PHPTRAVELS | Travel Technology Partner", "Title Mismatch"

    def test_login_page(self):
        self.driver.find_element_by_css_selector("div[class*='-login'] a").click()
        self.driver.find_element_by_link_text("Login").click()
        site_title = self.driver.title
        assert site_title == "Login", "Title Mismatch"
        self.driver.find_element_by_css_selector("input[name='username']").send_keys("user@phptravels.com")
        self.driver.find_element_by_css_selector("input[name='password']").send_keys("demouser")
        self.driver.find_element_by_css_selector("button[class*='loginbtn']").click()
        self.wait_for_element(self.driver,"img[class *='thumbnail']")
        site_title = self.driver.title
        assert site_title == "My Account", "Title Mismatch"
