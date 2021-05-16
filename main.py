import datetime as dt
import random
import smtplib
import pandas

USER = "iamgrace2113@gmail.com"
PASSWORD = "<YOUR_PASSWORD>"

now = dt.datetime.now()

birthday_info = pandas.read_csv("birthdays.csv")
new_dict = birthday_info.to_dict(orient="records")
for wish in range(len(new_dict)):
    detail = new_dict[wish]
    birth_day = detail["day"]
    birth_month = detail["month"]
    birth_name = detail["name"]
    birth_email = detail["email"]
    if now.day == birth_day and now.month == birth_month:
        with open(f"letter_templates/letter_{random.randint(1, 16)}.txt") as letter:
            birthday_wish = letter.read()

        with open(f'wishes/letter_{birth_name}', "w") as new_letter:
            new_wish = birthday_wish.replace("[NAME]", birth_name)
            new_letter.write(new_wish)

        with open(f'wishes/letter_{birth_name}') as letter_to_send:
            send = letter_to_send.read()
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER,
                                to_addrs=birth_email,
                                msg=f"Subject: Happy Birthday {birth_name}!\n\n{send}")
            connection.close()
