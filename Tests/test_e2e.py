from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

# child class
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        # 1. click on shop
        self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()  # a[href*='Shop'] partial value give

        # 2. find all products and add blackberry
        products = self.driver.find_elements(By.XPATH, "//app-card-list/app-card")

        for product in products:
            productName = product.find_element(By.XPATH, "div/div/h4").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/div[2]/button").click()

        # 3. click on checkout

        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        # 4. click on checkout on next page

        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        # 5. Find country, explicit wait, click on country, checkbox, checkout

        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
        self.driver.find_element(By.XPATH, "//a[text()='India']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        # 6. verify success text present on success msg
        expected_success_msg = 'Success! Thank you!'

        actual_success_msg = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        print(actual_success_msg)
        assert expected_success_msg in actual_success_msg
