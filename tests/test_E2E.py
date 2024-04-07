import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from testData.E2EData import E2EData

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, getData):

        expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        actualList = []

        homePage = HomePage(self.driver)
        homePage.enterTextInSearchFld(getData["search"])
        time.sleep(2)
        results = homePage.searchResults()
        count = len(results)

        assert count > 0
        for result in results:
            actualList.append(result.find_element(By.XPATH, "h4").text)
            result.find_element(By.XPATH, "div/button").click()

        homePage.clickCartBtn()
        checkOutPage = homePage.clickProceedToCheckoutBtn()

        prices = checkOutPage.price()
        sum = 0

        for price in prices:
            sum = sum + int(price.text)
        print(sum)

        totalAmount = int(checkOutPage.totalAmount())
        assert sum == totalAmount

        checkOutPage.enterPromoCode(getData["promo-code"])
        checkOutPage.clickApplyBtn()

        print(checkOutPage.getSuccessNotice())

        discountAmount = float(checkOutPage.getDiscountAmount())
        assert totalAmount > discountAmount

    @pytest.fixture(params=E2EData.test_E2EData)
    def getData(self, request):
        return request.param