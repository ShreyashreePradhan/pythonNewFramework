import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def Setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        service_obj = Service("C:\\Users\\SLP07848\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    # yield
    # driver.close()
