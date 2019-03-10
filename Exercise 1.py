#Exercise 1: Using CSS to locate an element and check its text

from selenium import webdriver

driver = webdriver.Firefox(executable_path = 'C:\geckodriver\geckodriver')
driver.get("http://tvroom.github.io/selenium-exercises/ex1/")
driver.implicitly_wait(10)
elem = driver.find_element_by_css_selector('h3.sel_header')

assert "Selenium Test Header" in elem.text


