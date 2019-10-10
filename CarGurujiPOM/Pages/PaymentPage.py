class PaymentPage():

    def __init__(self,driver):
        self.driver = driver

        self.paybycheck_xpath="//a[@class='cheque']"
    def click_paybycheck(self):
        self.driver.find_element_by_xpath(self.paybycheck_xpath).click()