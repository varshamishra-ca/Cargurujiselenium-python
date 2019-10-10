class ConfirmationPage():

    def __init__(self,driver):
        self.driver = driver

        self.confirmation_xpath="//button[@class='button btn btn-default button-medium']"

    def click_confirmation(self):
        self.driver.find_element_by_xpath(self.confirmation_xpath).click()