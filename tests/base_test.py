import os
import warnings
from pathlib import Path

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

        yield self.wait, self.driver

        self.take_screenshot('after_test', request.node.name)

        if self.driver is not None:
            self.driver.quit()

    def take_screenshot(self, name, function_name):
        screenshot_name = f'results/{function_name}_{name}.png'
        try:
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved as {screenshot_name}")
        except Exception as e:
            print(f"Failed to save screenshot: {e}")