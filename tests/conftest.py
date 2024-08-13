import pytest
import yaml
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils import data_generator, data_reader

logger = logging.getLogger(__name__)


@pytest.fixture(scope='class', autouse=True)
def setup_teardown():
    logger.info("Starting browser session")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("Ending browser session")


@pytest.fixture(scope='class')
def generate_customer_data():
    logger.info('Generating customer data')
    data_generator.generate_customer_data('../data')


@pytest.fixture(scope='class')
def read_customer_data():
    logger.info('Reading customer data')
    data = data_reader.read_data('../data/customer_data.json')
    logger.info(f'customer data is: {data[0]}')
    return data[0]


@pytest.fixture(scope='class')
def url():
    logger.info('Reading url')
    with open('../configurations/urls.yaml', 'r') as f:
        urls = yaml.safe_load(f)
    return urls
