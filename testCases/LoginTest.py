import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time

# To refer to pageObject need to import sys
sys.path.append('/home/flyboypk/Projects/UnitTestProject_POMBased')

from pageObjects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path='/home/flyboypk/Projects/UnitTestProject_POMBased/Drivers/chromedriver')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)  # Object for login page
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Website Title Mismatch")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/flyboypk/Projects/UnitTestProject_POMBased/reports'))
