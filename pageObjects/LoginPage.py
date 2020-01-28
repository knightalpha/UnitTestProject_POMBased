class LoginPage() :
    # Locators of all the elements
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input'
    link_logout_linktext = 'Logout'
    # link_logout_linkText = 'welcome'

    # Constructor to initiate the driver. This constructor will invoke whenever object for LoginPage reader is created.
    def __init__(self, driver):
        self.driver = driver

    # First action method for locators
    def setUserName(self, username ):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self, username):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()