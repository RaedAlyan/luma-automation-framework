import pytest
import allure
from random import randint
from keywords.products_keywords import purchase_men_product, purchase_women_product, purchase_gear_product
from configurations.constants import SUCCESS_MESSAGE


class TestProducts:

    @pytest.mark.parametrize('qty, product_type', [
        pytest.param(qty := randint(1, 10), 'hoodies and sweatshirts',
                     id=f'qty={qty}, product: hoodies and sweatshirts'),
        pytest.param(qty := randint(1, 10), 'jackets', id=f'qty={qty}, product: jackets'),
        pytest.param(qty := randint(1, 10), 'tees', id=f'qty={qty}, product: tees'),
        pytest.param(qty := randint(1, 10), 'bras and tanks', id=f'qty={qty}, product: bras and tanks'),
        pytest.param(qty := randint(1, 10), 'pants', id=f'qty={qty}, product: pants'),
        pytest.param(qty := randint(1, 10), 'shorts', id=f'qty={qty}, product: shorts')
    ])
    @allure.feature('Product Purchase')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that a user can purchase different types of products for women with '
                        'various quantities.')
    @allure.title('Test Purchase {product_type} Product for women')
    def test_purchase_women_product(self, setup_teardown, url, qty, product_type):
        self.driver = setup_teardown
        self.driver.get(url['women_page'])
        with allure.step(f'Purchasing {qty} {product_type} for women products'):
            success_message = purchase_women_product(self.driver, product_type, qty)
        with allure.step('Validating success message'):
            product_title = self.driver.title
            assert success_message == SUCCESS_MESSAGE.format(product_title)

    @pytest.mark.parametrize('qty, product_type', [
        pytest.param(qty := randint(1, 10), 'hoodies and sweatshirts',
                     id=f'qty={qty}, product: hoodies and sweatshirts'),
        pytest.param(qty := randint(1, 10), 'jackets', id=f'qty={qty}, product: jackets'),
        pytest.param(qty := randint(1, 10), 'tees', id=f'qty={qty}, product: tees'),
        pytest.param(qty := randint(1, 10), 'tanks', id=f'qty={qty}, product: tanks'),
        pytest.param(qty := randint(1, 10), 'pants', id=f'qty={qty}, product: pants'),
        pytest.param(qty := randint(1, 10), 'shorts', id=f'qty=,{qty} product: shorts'),
    ])
    @allure.feature('Product Purchase')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that a user can purchase different types of products for men with '
                        'various quantities.')
    @allure.title('Test Purchase {product_type} Product for men')
    def test_purchase_men_product(self, setup_teardown, url, qty, product_type):
        self.driver = setup_teardown
        self.driver.get(url['men_page'])
        with allure.step(f'Purchasing {qty} {product_type} for men products'):
            success_message = purchase_men_product(self.driver, product_type, qty)
        with allure.step('Validating success message'):
            product_title = self.driver.title
            assert success_message == SUCCESS_MESSAGE.format(product_title)

    @pytest.mark.parametrize('qty, product_type', [
        pytest.param(qty := randint(1, 10), 'bags', id=f'qty={qty}, product: bags'),
        pytest.param(qty := randint(1, 10), 'fitness_equipment',
                     id=f'qty={qty}, product: fitness equipment'),
        pytest.param(qty := randint(1, 10), 'watches', id=f'qty={qty}, product: watches'),
    ])
    @allure.feature('Product Purchase')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('This test verifies that a user can purchase different types of gear products with various '
                        'quantities.')
    @allure.title('Test Purchase {product_type} gear Product')
    def test_purchase_gear_product(self, setup_teardown, url, qty, product_type):
        self.driver = setup_teardown
        self.driver.get(url['gear_page'])
        with allure.step(f'Purchasing {qty} {product_type} for gear products'):
            success_message = purchase_gear_product(self.driver, product_type, qty)
        with allure.step('Validating success message'):
            product_title = self.driver.title
            assert success_message == SUCCESS_MESSAGE.format(product_title)
