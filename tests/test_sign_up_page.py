import logging
import pytest
import allure
from keywords.auth_keywords import sign_up
from pages.create_account_page import CreateAccountPage


class TestSignupPage:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    @allure.feature('Sign Up')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Test Sign Up feature')
    @pytest.mark.run(order=1)
    def test_signup(self, setup_teardown, generate_customer_data, read_customer_data, url):
        self.logger.info('Starting test_signup')
        self.driver = setup_teardown
        self.driver.get(url['sign_up'])
        with allure.step('Sign Up'):
            sign_up(self.driver, read_customer_data)
        with allure.step("Validating title"):
            sign_up_page = CreateAccountPage(self.driver)
            assert sign_up_page.get_title() == 'My Account'
        self.logger.info('test_signup completed successfully')
