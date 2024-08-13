import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class GearPage(BasePage):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    LOCATORS = {
        'bags': (By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li[1]/a'),
        'fitness_equipment': (By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li[2]/a'),
        'watches': (By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li[3]/a')
    }

    def __init__(self, driver):
        super().__init__(driver)

    def purchase_gear_product(self, qty, product_type):
        bags_locator = self.LOCATORS[product_type]
        if bags_locator:
            self.purchase(qty, bags_locator, product_type=product_type)
        else:
            self.logger.error('Can\'t get bags locator')
