class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.signout_xpath = "//a[@class='logout']"
        self.search_xpath = "//input[@id='search_query_top']"
        self.search_submit_xpath = "//button[@name='submit_search']"


    def click_signout(self):
        self.driver.find_element_by_xpath(self.signout_xpath).click()
    def searchan_item(self,item):
        self.driver.find_element_by_xpath(self.search_xpath).click()
        self.driver.find_element_by_xpath(self.search_xpath).send_keys(item)
        self.driver.find_element_by_xpath(self.search_submit_xpath).click()

