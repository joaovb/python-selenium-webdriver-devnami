from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://wayvermedia.com/iframe-demo.html")

driver.switch_to.frame('frame1')

