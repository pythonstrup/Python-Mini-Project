##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import random
import datetime as dt

MY_EMAIL = "pythonstrup@gmail.com"
PASSWORD = "asdf1123!"
TYPE_OF_LETTER = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv
data_file = pandas.read_csv("birthdays.csv")
data_dict = data_file.to_dict(orient="records")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for data in data_dict:
    if now.month == data["month"] and now.day == data["day"]:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        current_letter = random.choice(TYPE_OF_LETTER)
        with open(f"letter_templates/{current_letter}") as letter_file:
            lines = letter_file.readlines()
            x = lines[0].replace("[NAME]", f"{data['name']}")
            lines[0] = x

        letter = ""
        for line in lines:
            letter += line

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=data["email"],
                msg=f"Subject:Happy Birthday!! {data['name']}!!\n\n{letter}")



