class productpage():

    def __init__(self,driver):
        self.driver = driver

        self.addtocart_xpath  ="//p[@id='add_to_cart']"

    def click_addtocart(self):
        self.driver.find_element_by_xpath(self.addtocart_xpath).click()

