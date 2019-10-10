class Checkout():

    def __init__(self,driver):
        self.driver = driver

        self.ckeckout_xpath="//a[@class='btn btn-default button button-medium']"
    def click_checkout(self):
        self.driver.find_element_by_xpath(self.ckeckout_xpath).click()
