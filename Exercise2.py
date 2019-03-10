'''Test the following:

We are logged in as bob when supplying correct credentials
We are logged in as guest when we don't supply a bad password
We get an Incorrect Password error when supplying a bad password'''

from selenium import webdriver

driver = webdriver.Firefox(executable_path = 'C:\geckodriver\geckodriver')
driver.get("http://tvroom.github.io/selenium-exercises/ex2/")
user = driver.find_element_by_name('username').send_keys("bob")
pswd = driver.find_element_by_name('password').send_keys("foobarz")
xpath = '//input[@type="submit" and @value="Login"]'
bton = driver.find_element_by_xpath(xpath).click()
assert driver.find_element_by_class_name("error")
driver.implicitly_wait(5)

driver = webdriver.Firefox(executable_path = 'C:\geckodriver\geckodriver')
driver.get("http://tvroom.github.io/selenium-exercises/ex2/")
user2 = driver.find_element_by_name('username').send_keys("bob")
pswd2 = driver.find_element_by_name('password').send_keys("foobaz")
xpath = '//input[@type="submit" and @value="Login"]'
bton2 = driver.find_element_by_xpath(xpath).click()
driver.implicitly_wait(5)
logusr= driver.find_element_by_class_name("user")
assert logusr.text == 'bob'
