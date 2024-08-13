import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CreateAccountPage(BasePage):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    EMAIL = (By.ID, 'email_address')
    PASSWORD = (By.ID, 'password')
    CONFIRM_PASSWORD = (By.ID, 'password-confirmation')
    CREATE_ACCOUNT = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.logger.info(f'Entering first name: {first_name}')
        self.enter_text(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.logger.info(f'Entering last name: {last_name}')
        self.enter_text(self.LAST_NAME, last_name)

    def enter_email(self, email):
        self.logger.info(f'Entering email: {email}')
        self.enter_text(self.EMAIL, email)

    def enter_password(self, password):
        self.logger.info('Entering password')
        self.enter_text(self.PASSWORD, password)

    def enter_confirm_password(self, password):
        self.logger.info('Entering confirm password')
        self.enter_text(self.CONFIRM_PASSWORD, password)

    def click_create_account_button(self):
        self.logger.info('clicking create account button')
        self.click_element(self.CREATE_ACCOUNT)
