from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://wikipedia.org')

element = driver.find_element_by_link_text('Wiktionary')

hover = ActionChains(driver).move_to_element(element)

hover.perform()