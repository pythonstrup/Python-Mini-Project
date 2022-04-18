from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "C:\develop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.set_window_size(width=1900, height=800)


# Automatically Login In

MY_EMAIL = "pythonstrup@gmail.com"
PASSWORD = "asdf1123!"
driver.get("https://www.linkedin.com/")

id = driver.find_element_by_id("session_key")
password = driver.find_element_by_id("session_password")

id.send_keys(MY_EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)


# Apply for a Job
search = driver.find_element_by_class_name("search-global-typeahead__input")
search.send_keys("Python developer")
search.send_keys(Keys.ENTER)

time.sleep(3)
all_filter = driver.find_element_by_id("ember316")
all_filter.click()
time.sleep(3)
label = driver.find_element_by_xpath('//*[@id="ember322"]/ul/li[6]/fieldset/div/ul/li/label/p')
label.click()
show_button = driver.find_element_by_xpath('//*[@id="ember328"]/span')
show_button.click()

time.sleep(3)
save_button = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/button')
save_button.click()

job_search = driver.find_elements_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li")

for n in range(1, len(job_search)):
    time.sleep(3)
    job_search[n].click()
    time.sleep(3)
    save_button.click()
