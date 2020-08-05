from splinter import Browser

with Browser() as browser:
    url = 'https://aternos.org/go/'
    browser.visit(url)
    