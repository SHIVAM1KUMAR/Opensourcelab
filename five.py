import os
import math
import random
import smtplib
digits="0123456789"
OTP=""
for i in range(6):
 OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("YOUR EMAIL HERE ", "YOUR SECRET KEY HERE ")
emailid = input("Enter your email: ")
s.sendmail('HELO ',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
 print("Verified")
else:
 print("Please Check your OTP again")