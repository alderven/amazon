import os
import configparser
import selenium_methods

CONFIG = 'config.cfg'


class Base(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def config(self):
        cfg = configparser.ConfigParser()
        cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG)
        cfg.read(cfg_path)
        return cfg


class Home(Base):

    def open_page(self):
        return self.driver.get(self.config['SITE']['URL'])

    def search(self, product_name):
        selenium_methods.enter_text(self.driver, self.config['HOME']['SEARCH'], product_name)


class Results(Base):

    @property
    def total_count(self):
        element = selenium_methods.find_element(self.driver, self.config['RESULTS']['TOTAL_COUNT']).text
        # sample text is "1-48 of 597 results for " => so split to list anf get second element i.e. "597"
        return int(''.join(filter(str.isdigit, element.split()[2])))
