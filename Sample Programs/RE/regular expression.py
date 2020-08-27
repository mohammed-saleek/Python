'''
import re
num=input('enter the number:')
def number(num):
    pattern=re.compile('[0/91]?[7-9][0-9]{10}')
    return pattern.match(num)
    
    if(isValid(num)):
        print('valid number')
    else:
        print('WARNING...print valid number')
number(num)


    
import re
num=input('enter the phone number:')
def sample(num):
    k=re.search(pattern="(\s)(\d)[@][gmail]+.(\s){3}",string=num)
    return k
if (sample(num)):
    print(f'is the valid num:',num)
else:
    print('WARNING...it is invalid number')

'''
import re
gmail=input('Enter the Gmail Id:')
def demo(gmail):
    mail=re.search("^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$",string=gmail)
    return mail
if(demo(gmail)):
    print('Gmail id is valid',gmail)
else:
    print('Gmail id is not valid',gmail)

