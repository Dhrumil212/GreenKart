from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
    results = (By.XPATH, "//div[@class='products']/div")
    cartBtn = (By.XPATH, "//img[@alt='Cart']")
    proceedToCheckoutBtn = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def enterTextInSearchFld(self, text):
        return self.driver.find_element(*HomePage.search).send_keys(text)

    def searchResults(self):
        return self.driver.find_elements(*HomePage.results)

    def clickCartBtn(self):
        return self.driver.find_element(*HomePage.cartBtn).click()

    def clickProceedToCheckoutBtn(self):
        self.driver.find_element(*HomePage.proceedToCheckoutBtn).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
