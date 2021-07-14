import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def site_setup(request):
    driver = webdriver.Chrome(executable_path="/home/arun/selenium/chromedriver")
    driver.get("https://www.phptravels.net/home")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()