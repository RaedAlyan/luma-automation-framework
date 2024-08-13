import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WomenPage(BasePage):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    LOCATORS = {
        'hoodies and sweatshirts': (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a'),
        'jackets': (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[2]/a'),
        'tees': (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[3]/a'),
        'bras and tanks': (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[4]/a'),
        'pants': (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[2]/li[1]/a'),
        'shorts': (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[2]/li[2]/a')
    }

    def __init__(self, driver):
        super().__init__(driver)

    def purchase_women_product(self, qty, product_type):
        product_type_locator = self.LOCATORS.get(product_type)
        if product_type_locator:
            self.logger.info(f'Purchasing {product_type} product with {qty} quantities')
            self.purchase(qty=qty, product_type_locator=product_type_locator)
            self.logger.info('Product purchased successfully')
        else:
            self.logger.error(f'Invalid product type: {product_type}')

