from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

executable_path = {'executable_path': ChromeDriverManager().install()}

with Browser('chrome', **executable_path) as browser:
    url = 'https://aternos.org/go/'
    browser.visit(url)
    browser.find_by_id('user').fill('')
    browser.find_by_id('password').fill('')
    browser.find_by_id('login').click()
    browser.visit('https://aternos.org/server/')
    time.sleep(20)
    