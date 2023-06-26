import smtplib

email = "abcd123@gmail.com"
my_password = "123456789pass"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= email, password= my_password)
connection.sendmail(from_addr=email, to_addrs="abc098@yahoo.com", msg="Subject:Hello\n\nthis is a msg")
connection.close()


# if you don't want to use close method u can try with method like file opening

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= email, password= my_password)
#     connection.sendmail(from_addr=email, to_addrs="abc098@yahoo.com", msg="Subject:Hello\n\nthis is a msg")