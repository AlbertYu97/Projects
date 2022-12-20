
import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "furthermoker@gmail.com"
MY_PASSWORD = "drarlyxtqpfpadjy"
letter_list = ["letter_1", "letter_2", "letter_3"]

# 1. Update the birthdays.csv
birthday = pd.read_csv("birthdays.csv")
bd_dict = birthday.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
for item in bd_dict:
    if item['month'] == month and item['day'] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(letter_list)
        with open(f"letter_templates/{letter}.txt") as birthday_letter:
            birthday_letter = birthday_letter.read().replace("[NAME]", f"{item['name']}")
            # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="furthermoker@yahoo.com",
                msg=f"Subject:Happy birthday\n\n{birthday_letter}"
            )



