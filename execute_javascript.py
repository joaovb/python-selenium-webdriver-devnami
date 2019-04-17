from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://en.wikipedia.org")

driver.execute_script("window.alert('This is alert');")

