import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="S:\Selenium\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()