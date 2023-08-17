import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser(request):

    options = webdriver.ChromeOptions()
    # options.add_argument("--kiosk")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser
    browser.quit()
