from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time 

driver = webdriver.Chrome()
driver.get("http://google.com")
elem = driver.find_element_by_tag_name("body")
time.sleep(5)
elem.send_keys(Keys.CONTROL+"t")
time.sleep(5)
elem.send_keys(Keys.CONTROL+"w")