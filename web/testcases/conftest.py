from web.config.driver_config import getSeleniumDriver
import pytest


driver = None


@pytest.fixture()
def chrome_driver():
    global driver
    driver = getSeleniumDriver()
    yield driver
    driver.quit()

