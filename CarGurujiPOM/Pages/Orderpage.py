from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Orderpage():

    def __init__(self,driver):
        self.driver = driver

        self.proceedtocheckout_xpath="//a[@class='button btn btn-default standard-checkout button-medium']"

    def click_proceedtocheckout(self):
        #wait= WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.proceedtocheckout_xpath))
        self.driver.find_element_by_xpath(self.proceedtocheckout_xpath).click()