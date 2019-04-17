from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://google.com')

try:
    assert 'Google' in browser.title
    print('Assertion test pass')

except Exception as e:
    print('Assertion test failed', format(e))

browser.close()