from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://google.com')

element=driver.find_element_by_id('gsr')

location = element.location
size = element.location

print(location)
print(size)