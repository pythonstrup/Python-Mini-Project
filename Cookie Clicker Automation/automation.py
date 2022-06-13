from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "C:\develop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

f_name.send_keys("HeungMin")
l_name.send_keys("Son")
email.send_keys("son@gmail.com")
button = driver.find_element_by_class_name("btn-primary")
button.send_keys(Keys.ENTER)

