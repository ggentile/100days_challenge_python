import smtplib
import datetime as dt
import random
import os
import pandas


anniversariants = pandas.read_csv("birthdays.csv")
people = anniversariants.to_dict(orient="records")

my_email = "mrgiannitest@gmail.com"
password = "u1k3%(3I!1H"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

for person in people:
    tuple_person = (person["month"], person["day"])
    file_to_read = random.choice(os.listdir("letter_templates"))
    full_path = "C:\\Users\\giann\\PycharmProjects\\mail_send\\letter_templates\\" + file_to_read
    if tuple_person == today_tuple:
        with open(full_path, mode="r") as file:
            line = file.read()
            message = line.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="y.mrtest@yahoo.com",
                        msg=f"Subject:Happy Birthday!\n\n{message}")
