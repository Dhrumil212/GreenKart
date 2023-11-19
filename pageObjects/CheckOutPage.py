from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from utilities.BasePage import BasePage


class CheckOutPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    priceColumn = (By.XPATH, "//tr/td[5]/p")
    totAmount = (By.CLASS_NAME, "totAmt")
    promoCode = (By.CLASS_NAME, "promoCode")
    applyBtn = (By.CLASS_NAME, "promoBtn")
    codeApplied = (By.CLASS_NAME, "promoInfo")
    discountAmount = (By.CLASS_NAME, "discountAmt")

    def price(self):
        return self.driver.find_elements(*CheckOutPage.priceColumn)

    def totalAmount(self):
        return self.driver.find_element(*CheckOutPage.totAmount).text

    def enterPromoCode(self, text):
        return self.driver.find_element(*CheckOutPage.promoCode).send_keys(text)

    def clickApplyBtn(self):
        self.driver.find_element(*CheckOutPage.applyBtn).click()
        #return self.verifyLinkPresence().until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
        return self.verifyLinkPresence().until(expected_conditions.presence_of_element_located(self.codeApplied))
        #return self.driver.find_element(*CheckOutPage.applyBtn).click()

    def getSuccessNotice(self):
        return self.driver.find_element(*CheckOutPage.codeApplied).text

    def getDiscountAmount(self):
        return self.driver.find_element(*CheckOutPage.discountAmount).text
