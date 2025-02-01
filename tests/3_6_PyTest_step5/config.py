import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"  # Укажите здесь правильный путь
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)