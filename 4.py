# code no : 4
# 1-April-2020


import smtplib

from_email = str(input("From email :-"))
to_email = str(input("To email :-"))
password = str(input("Password :-"))

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(from_email, password)

message = """Subject:---THIS IS THE SUBJECT---


        ---THIS IS THE BODY OF THE MESSAGE---
        """

s.sendmail(from_email, to_email, message)

s.quit()
