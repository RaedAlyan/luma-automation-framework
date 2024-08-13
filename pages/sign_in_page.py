import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'pass')
    SIGN_IN_BUTTON = (By.ID, 'send2')
    FORGET_PASSWORD_LINK = (By.XPATH, '//*[@id="login-form"]/fieldset/div[4]/div[2]/a')
    CREATE_ACCOUNT_LINK = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[2]/div[2]/div/div/a')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.logger.info(f'Entering email: {email}')
        self.enter_text(self.EMAIL, email)

    def enter_password(self, password):
        self.logger.info('Entering password')
        self.enter_text(self.PASSWORD, password)

    def click_sign_in_button(self):
        self.logger.info('Clicking sign in button')
        self.click_element(self.SIGN_IN_BUTTON)

    def click_forget_password_link(self):
        self.logger.info('Clicking forget password link')
        self.click_element(self.FORGET_PASSWORD_LINK)

    def click_create_account_link(self):
        self.logger.info('Clicking create account link')
        self.click_element(self.CREATE_ACCOUNT_LINK)
