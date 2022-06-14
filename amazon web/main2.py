from selenium import webdriver
import smtplib

MAIL = "YOUR_MAIL"
PASSWORD = "YOUR_PASS_WORD"

driver_path = "C:\develop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get("https://www.amazon.com/Garmin-Forerunner-Easy-Running-Watch/dp/B01KPUHBK6/ref=sr_1_4?dchild=1&keywords=watch&qid=1629254875&sr=8-4")

price_lo = driver.find_element_by_id("priceblock_ourprice").text

price = float(price_lo.replace("$", ""))
print(price)

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=MAIL,
            msg=f"Instant Garmin 010-01689-00 Forerunner 35; Easy-to-Use GPS Running Watch, Black is now ${price}"
        )