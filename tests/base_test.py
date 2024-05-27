import os
import warnings
from pathlib import Path
import logging
import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'

def config():
    path = Path(__file__).parent / "../data/config.yml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()

class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self, request):
        warnings.simplefilter("ignore", ResourceWarning)
        cfg = config()
        if cfg['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            if cfg['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        elif cfg['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if cfg['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        if not os.path.exists('results'):
            os.makedirs('results')

        self.setup_logging(request.node.name)

        self.logger.info("Initialized driver and opened browser.")

        yield self.wait, self.driver

        self.take_screenshot('after_test', request.node.name)

        self.logger.info("Test completed and browser closed.")

        if self.driver is not None:
            self.driver.quit()

    def take_screenshot(self, name, function_name):
        screenshot_name = f'results/{function_name}_{name}.png'
        try:
            self.driver.save_screenshot(screenshot_name)
            self.logger.info(f"Screenshot saved as {screenshot_name}")
        except Exception as e:
            self.logger.error(f"Failed to save screenshot: {e}")

    def setup_logging(self, function_name):
        log_file = f'results/{function_name}.log'
        logger = logging.getLogger(function_name)
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler(log_file, mode='w')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        self.logger = logger
        self.logger.info(f"Logging setup complete for {function_name}")
