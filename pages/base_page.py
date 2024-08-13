import logging
import random
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    def find_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_success_message(self):
        return self.wait.until(ec.visibility_of_element_located((
            By.XPATH, "//div[@role='alert']//div[contains(@class, 'message-success')]"))).text

    def set_quantity(self, quantity):
        self.logger.info('Setting quantity')
        quantity_input_locator = (By.ID, 'qty')
        self.enter_text(quantity_input_locator, quantity)

    def click_size(self):
        self.logger.info('Selecting size')
        size_options_locator = (By.CSS_SELECTOR, 'div[attribute-code="size"]')
        size_options = self.find_element(size_options_locator)
        time.sleep(5)
        size_options_list = size_options.find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
        time.sleep(5)
        sizes = size_options_list.find_elements(By.TAG_NAME, 'div')
        random_index = random.randint(0, len(sizes) - 1)
        sizes[random_index].click()

    def click_color(self):
        self.logger.info('Selecting color')
        color_options_locator = (By.CSS_SELECTOR, 'div[attribute-code="color"]')
        color_options = self.find_element(color_options_locator)
        time.sleep(5)
        colors_options_list = color_options.find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
        time.sleep(5)
        colors = colors_options_list.find_elements(By.TAG_NAME, 'div')
        random_index = random.randint(0, len(colors) - 1)
        colors[random_index].click()

    def purchase(self, qty, product_type_locator, product_type=None):
        self.click_element(product_type_locator)
        main_list_product_locator = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol')
        product_lists_locator = (By.TAG_NAME, 'li')
        main_list_product = self.find_element(main_list_product_locator)
        time.sleep(5)
        products = main_list_product.find_elements(*product_lists_locator)
        random_index = random.randint(0, len(products) - 1)
        products[random_index].click()
        if product_type is None:
            self.click_size()
            self.click_color()
        self.set_quantity(qty)
        cart_button_locator = (By.ID, 'product-addtocart-button')
        self.click_element(cart_button_locator)
        self.logger.info('Product added to cart')
