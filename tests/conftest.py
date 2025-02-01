import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, fr, ru, etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if not user_language:
        raise pytest.UsageError("--language should be specified")

    options = FirefoxOptions()
    options.set_preference("intl.accept_languages", user_language)
    print(f"\nstart firefox browser for test with language {user_language}..")
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()