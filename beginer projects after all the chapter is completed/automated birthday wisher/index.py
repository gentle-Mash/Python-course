import pandas
import random
import datetime as dt
import smtplib

email = "deku123@yahoo.com"
my_password = "123456789abc#"

today = dt.datetime.now()
t_day,t_month = today.day,today.month

birthday_info = pandas.read_csv("birthdays.csv")
birthday_person = {row.name:row for (index,row) in birthday_info.iterrows()}

letters = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
with open (random.choice(letters)) as letter_data:
    data = letter_data.read()

    for day, month in birthday_person.items():
        if (t_day == month.day) and (t_month == month.month):
            data = data.replace("[NAME]", month.username)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email, password=my_password)
                connection.sendmail(from_addr=email, to_addrs=month.email, msg=f"Subject:Happy Birthday\n\n{data}")