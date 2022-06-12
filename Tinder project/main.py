from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

ID = "YOUR_ID"
PASSWORD = "YOUR_PASSWORD"

driver_path = "C:\develop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://tinder.com/")

time.sleep(3)
login_button = driver.find_element_by_class_name("button")
login_button.click()
time.sleep(3)
facebook = driver.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)

time.sleep(3)
email = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email.send_keys(ID)
password = driver.find_element_by_name("pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow = driver.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div/div/div[3]/button[1]')
allow.click()
time.sleep(3)
activate = driver.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div/div/div[3]/button[1]')
activate.click()
time.sleep(3)
agree = driver.find_element_by_xpath('//*[@id="u-648818393"]/div/div[2]/div/div/div[1]/button')
agree.click()




try:
    pass_button = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
    time.sleep(3)
    pass_button.click()

except ElementClickInterceptedException:
    try:
        time.sleep(1)
        uninteresting = driver.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div[2]/button[2]')
        uninteresting.click()

    except NoSuchElementException:
        time.sleep(2)
