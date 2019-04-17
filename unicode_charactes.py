from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://en.wikipedia.org')
element = driver.find_element_by_css_selector('body')
time.sleep(5)
element.send_keys('\uE035')