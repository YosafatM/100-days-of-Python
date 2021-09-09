import smtplib
import datetime as dt
import random as rd

EMAIL = ""
PASSWORD = ""

time = dt.datetime.now()
day_number = time.weekday()

if day_number == 3:
    with open("quotes.txt") as handle:
        lines = handle.readlines()
        quote = rd.choice(lines)

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="yosafatmartinez21@gmail.com",
            msg=f"Subject: Thursday motivation\n\n{quote}"
        )
