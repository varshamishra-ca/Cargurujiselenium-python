class SigninPage():

    def __init__(self,driver):
        self.driver = driver

        self.Email_xpath = "//input[@id='email']"
        self.pwd_xpath = "//input[@id='passwd']"
        self.submit_xpath = "//button[@id='SubmitLogin']"


    def enter_signin(self,mail,password):
        self.driver.find_element_by_xpath(self.Email_xpath).send_keys(mail)
        self.driver.find_element_by_xpath(self.pwd_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.submit_xpath).click()
        self.driver.implicitly_wait(10)

