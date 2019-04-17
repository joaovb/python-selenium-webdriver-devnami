from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://en.wikipedia.org')

element = driver.find_element_by_id('mp-dyk')

print(element.text)