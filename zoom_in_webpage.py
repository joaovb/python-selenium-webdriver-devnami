from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://en.wikipedia.org")
driver.execute_script("document.body.style.zoom='150%'")

