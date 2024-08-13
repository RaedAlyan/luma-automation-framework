import logging
import pytest
import allure
from keywords.auth_keywords import sign_in
from pages.sign_in_page import SignInPage


class TestSignInPage:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    @allure.feature("Sign in")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies the sign in feature')
    @pytest.mark.run(order=2)
    def test_sign_in(self, setup_teardown, read_customer_data, url):
        self.logger.info('Starting test_sign_in')
        self.driver = setup_teardown
        self.driver.get(url['sign_in'])
        with allure.step('Sign in page'):
            sign_in(self.driver, read_customer_data)
        with allure.step("Validating title"):
            sign_in_page = SignInPage(self.driver)
            assert sign_in_page.get_title() == 'My Account'
        self.logger.info('test_sign_in completed successfully')
