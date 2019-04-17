from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://wikipedia.org')

element = driver.find_element_by_link_text('Wiktionary')

actionChains = ActionChains(driver)

actionChains.context_click(element).perform()