from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.uol.com.br/')

for element in driver.find_element_by_tag_name('img'):
    print(element.text)
    print(element.tag_name)
    print(element.location)
    print(element.size)
