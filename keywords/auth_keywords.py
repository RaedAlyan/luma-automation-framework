import logging
from pages.sign_in_page import SignInPage
from pages.create_account_page import CreateAccountPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def sign_in(driver, customer_data):
    logger.info('Starting sign-in process')
    sign_in_page = SignInPage(driver)
    sign_in_page.enter_email(customer_data['email'])
    sign_in_page.enter_password(customer_data['password'])
    sign_in_page.click_sign_in_button()
    logger.info('Sign-in process completed')


def sign_up(driver, customer_data):
    logger.info('Starting sign-up process')
    sign_up_page = CreateAccountPage(driver)
    sign_up_page.enter_first_name(customer_data['first_name'])
    sign_up_page.enter_last_name(customer_data['last_name'])
    sign_up_page.enter_email(customer_data['email'])
    sign_up_page.enter_password(customer_data['password'])
    sign_up_page.enter_confirm_password(customer_data['password'])
    sign_up_page.click_create_account_button()
    logger.info('Sign-up process completed')
