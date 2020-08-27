#Email

import re

email=input("Enter Your Email id:")
def email_fun(email):
    pattern = re.search("^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$",string=email)
    return pattern

if (email_fun(email)):
    print("Valid Email")
else:
    print("Invalid")

email_fun(email)
    
