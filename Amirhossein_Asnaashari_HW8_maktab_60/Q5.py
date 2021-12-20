import re

phone_number = '+0989121111111'

form = '^\+0*989\d{9}$'

if re.search(form, phone_number):
    print("valid number")
else:
    print("invalid number")
