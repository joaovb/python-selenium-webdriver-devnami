from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://en.wikipedia.org")

ids = driver.find_element_by_xptah('//*[@name]')

for ii in ids:
    print(ii.get_attribute('name'))