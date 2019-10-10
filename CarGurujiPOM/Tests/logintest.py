import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import unittest

from CarGurujiPOM.Pages.SigninPage import SigninPage
from CarGurujiPOM.Pages.Homepage import HomePage
from CarGurujiPOM.Pages.dresssearch import Dresssearch
from CarGurujiPOM.Pages.checkout import Checkout
from CarGurujiPOM.Pages.Orderpage import Orderpage
from CarGurujiPOM.Pages.Addresspage import Addresspage
from CarGurujiPOM.Pages.Shippingpage import ShippingPage
from CarGurujiPOM.Pages.PaymentPage import PaymentPage
from CarGurujiPOM.Pages.ConfirmationPage import ConfirmationPage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome(executable_path ="/Users/sumit/Desktop/CACC Barsha/SeleniumIntro/CarGurujiPOM/drivers/chromedriver")
        cls.driver.implicitly_wait(5)
    def test_Alogin(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account")
        print(driver.title)
        self.driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/SeleniumIntro/CarGurujiPOM/Screenshots/landingpage.png")


        login= SigninPage(driver)
        login.enter_signin("sweetycacc@gmail.com","OS6t61SK")
        driver.implicitly_wait(10)
        title=driver.title
        self.assertEqual("My account - CarGuruji Shop", title,)
        self.driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/SeleniumIntro/CarGurujiPOM/Screenshots/Homepage.png")

        logout=HomePage(driver)

        logout.click_signout()
        self.driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/SeleniumIntro/CarGurujiPOM/Screenshots/Loggedout.png")
    def test_Baddtocart(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/login?back=my-account")

        login = SigninPage(driver)
        login.enter_signin("sweetycacc@gmail.com", "OS6t61SK")
        driver.implicitly_wait(10)
        search= HomePage(driver)
        search.searchan_item("dress")
        driver.implicitly_wait(3)
        clickoncart= Dresssearch(driver)
        clickoncart.click_addtocart()
        clickcheckout=Checkout(driver)
        clickcheckout.click_checkout()
        clickproceed = Orderpage(driver)
        driver.implicitly_wait(10)
        clickproceed.click_proceedtocheckout()
        click=Addresspage(driver)
        click.click_checkout()
        c=ShippingPage(driver)
        c.click_proceedcheckout()
        P=PaymentPage(driver)
        P.click_paybycheck()
        con=ConfirmationPage(driver)
        con.click_confirmation()
        confpage=driver.title
        print(confpage)
        self.assertEqual("Order confirmation - CarGuruji Shop", confpage)
        self.driver.get_screenshot_as_file("/Users/sumit/Desktop/CACC Barsha/SeleniumIntro/CarGurujiPOM/Screenshots/OrderConfirmation.png")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/sumit/Desktop/CACC Barsha/SeleniumIntro/CarGurujiPOM/Reports/Carguruji"),verbocity=2)



