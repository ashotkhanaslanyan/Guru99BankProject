import os
import warnings
from pathlib import Path
import shutil
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

    @pytest.fixture(scope='session', autouse=True)
    def clean_results(self):
        results_dir = Path('results')
        if results_dir.exists() and results_dir.is_dir():
            shutil.rmtree(results_dir)
        results_dir.mkdir(parents=True, exist_ok=True)
        yield

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

        class_name = request.node.cls.__name__

        class_results_dir = f'results/{class_name}'
        if not os.path.exists(class_results_dir):
            os.makedirs(class_results_dir)

        self.setup_logging(class_name, request.node.name)

        self.logger.info("Initialized driver and opened browser.")

        yield self.wait, self.driver

        self.take_screenshot('after_test', class_name, request.node.name)

        self.logger.info("Test completed and browser closed.")

        if self.driver is not None:
            self.driver.quit()

    def take_screenshot(self, name, class_name, function_name):
        screenshot_name = f'results/{class_name}/{function_name}_{name}.png'
        try:
            self.driver.save_screenshot(screenshot_name)
            self.logger.info(f"Screenshot saved as {screenshot_name}")
        except Exception as e:
            self.logger.error(f"Failed to save screenshot: {e}")

    def setup_logging(self, class_name, function_name):
        if not os.path.exists('results'):
            os.makedirs('results')

        global_log_file = 'results/log.log'
        global_fh = logging.FileHandler(global_log_file, mode='a')
        global_fh.setLevel(logging.INFO)
        global_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        global_fh.setFormatter(global_formatter)

        logger = logging.getLogger(function_name)
        logger.setLevel(logging.INFO)

        class_log_file = f'results/{class_name}/{function_name}.log'
        class_fh = logging.FileHandler(class_log_file, mode='w')
        class_fh.setLevel(logging.INFO)
        class_fh.setFormatter(global_formatter)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(global_formatter)

        logger.addHandler(global_fh)
        logger.addHandler(class_fh)
        logger.addHandler(ch)

        self.logger = logger
        self.logger.info(f"Starting {function_name}")
