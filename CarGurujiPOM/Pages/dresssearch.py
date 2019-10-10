class Dresssearch():

    def __init__(self,driver):
        self.driver = driver

        self.addtocart_xpath = "//span[contains(text(),'Add to cart')]"
        self.printeddress_xpath = "//a[@title='Printed Dress']"
    def click_addtocart(self):
        self.driver.find_element_by_xpath(self.printeddress_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.addtocart_xpath).click()