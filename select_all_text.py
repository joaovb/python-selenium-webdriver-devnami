from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("http://google.com")
element = driver.find_element_by_css_selector('body')
time.sleep(8)

element.send_keys(Keys.CONTROL+'a')
