import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language for browser: es, fr, ru, etc.')
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    chosen_browser = request.config.getoption('browser')

    if chosen_browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif chosen_browser == 'firefox':
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('intl.accept_languages', language)
        # browser = webdriver.Firefox(firefox_profile=profile)

        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Invalid browser choice: {chosen_browser}. Choose 'chrome' or 'firefox'.")

    browser.implicitly_wait(5)

    yield browser

    print('\nQuit browser..')
    browser.quit()