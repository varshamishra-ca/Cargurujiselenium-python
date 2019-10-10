class Addresspage():

    def __init__(self,driver):
        self.driver = driver

        self.proceedtocheckout_xpath="//button[@name='processAddress']"

    def click_checkout(self):
        self.driver.find_element_by_xpath(self.proceedtocheckout_xpath).click()


