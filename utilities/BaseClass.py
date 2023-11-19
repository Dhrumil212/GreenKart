import pytest
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self):
        return WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    #def verifyLinkPresence(self, text):
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))