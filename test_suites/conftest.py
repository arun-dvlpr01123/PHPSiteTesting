import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Select Option chrome or firefox"
    )


@pytest.fixture(scope="class")
def site_setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/home/arun/selenium/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/home/arun/selenium/geckodriver")
    driver.get("https://www.phptravels.net/home")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="function")
def site_setup_method(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="/home/arun/selenium/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="/home/arun/selenium/geckodriver")
    driver.get("https://www.phptravels.net/home")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()