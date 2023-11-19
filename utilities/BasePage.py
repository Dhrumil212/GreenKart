from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def verifyLinkPresence(self):
        return WebDriverWait(self.driver, 10)