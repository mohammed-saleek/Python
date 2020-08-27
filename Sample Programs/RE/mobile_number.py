#Mobile Number Pattern

import re
number = input("Enter Your Phone Number:")
def mobile_number(number):
        pattern = re.search("(0/91)?[7-9][0-9]{10}",number)
        return pattern


if (mobile_number(number)):
    print("Number Saved")
else:
    print("Invaid Number!!!...Try again")



mobile_number(number)
        
 
