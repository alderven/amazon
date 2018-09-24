# General information

This project contains simple UI test written in Python+Selenium and [Allure Report](https://cdn.rawgit.com/alderven/amazon/master/allure-report/index.html)

# Test Case and Test Result:
№ | Test Script                                                                                                                       | Run Result                                                                                                       
-- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- 
1  | [test_amazon_add_to_the_shopping_cart.py](https://github.com/alderven/amazon/blob/master/test_amazon_add_to_the_shopping_cart.py) | [Passed](https://cdn.rawgit.com/alderven/amazon/master/allure-report/index.html#packages/a3ba69d38a1588df4d97ea47e185269a/5aedd3359b72a51a/)  


# How to install
1. Download and unzip this project: https://github.com/alderven/amazon/archive/master.zip
1. Install Python 3.6 or higher: https://www.python.org/downloads/
1. Install following Python libs:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * selenium: https://pypi.python.org/pypi/selenium
   * allure-pytest: https://pypi.python.org/pypi/allure-pytest
   * configparser: https://pypi.python.org/pypi/configparser
1. Download ChromeDriver driver to the project root folder:
   http://chromedriver.chromium.org/downloads
1. Install Allure Framework. See detailed instruction: https://docs.qameta.io/allure/latest/


# How to run tests
Execute following line in CMD in the project folder:
```
python -m pytest --alluredir /full/path/to/report/folder
```

# How to generate Allure report
Execute following line in CMD in the project folder:
```
allure serve /full/path/to/report/folder
```