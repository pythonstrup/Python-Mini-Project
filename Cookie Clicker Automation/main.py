from selenium import webdriver

chrome_driver_path = "C:\develop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Amazon homepage
# driver.get("https://www.amazon.com/Apple-Watch-Space-Aluminum-Black/dp/B0799R5M8P/ref=sr_1_13?dchild=1&keywords=watch&qid=1629175886&sr=8-13")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


# Python homepage
driver.get('https://www.python.org/')
# search_bar = driver.find_element_by_name('q')
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath("//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

menu_dict = {}
proto_menu = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

name = [name.text for name in driver.find_elements_by_xpath("//*[@id='content']/div/section/div[2]/div[2]/div/ul/li/a")]
# year = [year.text for year in driver.find_elements_by_css_selector(".menu span")]
time = [time.text for time in driver.find_elements_by_css_selector(".menu time")]

for i in range(5):
    menu_dict[i] = {"time": time[i], "name": name[i]}

print(menu_dict)

driver.quit()

