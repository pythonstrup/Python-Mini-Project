from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

timeout = time.time() + 5
five_min = time.time() + 60*5

driver_path = "C:\develop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

proto = [price.text for price in driver.find_elements_by_css_selector("#store div b")]
price_list = []
for i in range(len(proto)-1):
    price = proto[i].split(" - ")[1]
    price = price.replace(",", "")
    price_list.append(int(price))

store = [thing for thing in driver.find_elements_by_css_selector("#store div")]
store.pop()


print(price_list)
while True:
    cookie.click()
    money = driver.find_element_by_id("money")
    my_cookie = int(money.text)
    hightest = store[0]

    if time.time() > timeout:
        for i in range(len(price_list)):
            if price_list[i] < my_cookie:
                hightest = store[i]


        hightest.click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break



