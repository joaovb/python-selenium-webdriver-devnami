from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.com')

cookie = {'fruit':'mango','chocolate':'milk'}
driver.add_cookie(cookie)
print(driver.get_cookies())