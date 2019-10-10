class ShippingPage():

    def __init__(self,driver):
        self.driver = driver

        self.termsandcondition_xpath="//input[@id='cgv']"
        self.proceedcheckout_xpath="//button[@name='processCarrier']"

    def click_proceedcheckout(self):
        self.driver.find_element_by_xpath(self.termsandcondition_xpath).click()
        self.driver.find_element_by_xpath(self.proceedcheckout_xpath).click()
