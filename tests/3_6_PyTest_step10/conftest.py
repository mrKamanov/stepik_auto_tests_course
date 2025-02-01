import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем параметр --language
def pytest_addoption(parser):
    parser.addoption(
        '--language',  # Название параметра
        action='store',  # Тип действия
        default='en',  # Значение по умолчанию
        help="Choose language: en, es, fr, ru, etc."  # Описание параметра
    )

# Фикстура для инициализации WebDriver
@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра --language
    user_language = request.config.getoption("language")

    # Настройка языка браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Инициализация WebDriver
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()  # Закрываем браузер после выполнения теста