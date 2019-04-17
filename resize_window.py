from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://wikipedia.org')
time.sleep(2)
browser.set_window_size(1024,768)
time.sleep(3)
print(browser.get_window_size())
time.sleep(3)
browser.maximize_window()
print(browser.get_window_size())
browser.close()