from pages.women_page import WomenPage
from pages.men_page import MenPage
from pages.gear_page import GearPage


def purchase_men_product(driver, product, qty):
    men_page = MenPage(driver)
    men_page.purchase_men_product(qty, product)
    return men_page.get_success_message()


def purchase_women_product(driver, product, qty):
    women_page = WomenPage(driver)
    women_page.purchase_women_product(qty, product)
    return women_page.get_success_message()


def purchase_gear_product(driver, product, qty):
    gear_page = GearPage(driver)
    gear_page.purchase_gear_product(qty, product)
    return gear_page.get_success_message()
