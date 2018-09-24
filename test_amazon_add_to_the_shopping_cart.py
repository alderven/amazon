import pytest
from pages import Home, Results


@pytest.allure.feature('Amazon')
@pytest.allure.story('Add to the shopping cart')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_amazon_add_to_the_shopping_cart(driver):

    with pytest.allure.step('1. Open Amazon homepage'):
        home = Home(driver)
        home.open_page()

    with pytest.allure.step('2. Search for any product (verify search input field and search button)'):
        product_name = 'Black Sabbath T-Shirt'
        home.search(product_name)

    with pytest.allure.step('3. Verify found results (please explain fragility of tests here and how we can fix it if '
                            'we own the product).'):

        # N.B. Fragility of the test depends on how many goods are available and whether this good is available at all.
        # To make test more stable we can add some "test" goods to the database and then search it.

        total_count = Results(driver).total_count
        assert total_count, 'No results found for product: "{}"'.format(product_name)
