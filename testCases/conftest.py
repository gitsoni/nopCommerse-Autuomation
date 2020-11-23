from selenium import webdriver

import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="/Users/sidmenu/PycharmProjects/nopcommerceApp/drivers/chromedriver")
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Ie()
    return driver

# For browser options during the test run
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

### Pytest html report generation ###

# Hook for adding environment info to html report
'''
def pytest_configure(config):
    config.metadata['Project Name'] = 'nop commerce'
    config.metadata['Module Name'] = 'Customers'

# Hook for deleting/modifying Environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
'''





