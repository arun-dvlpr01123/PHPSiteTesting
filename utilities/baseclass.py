import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("site_setup")
class Baseclass:

    def wait_for_element(self, driver, locator):

        # wait 10 seconds before looking for element
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator))
        )
