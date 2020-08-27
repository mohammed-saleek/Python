#To get gmail from a file

import re

dic={}
#Getting the file name
def gmail_from_file():
    
    while True:
        try:
            f = input("Enter the file name to open:")
            filename = open(f,'r')
        except Exception as e:
            print("The File doesn't Exist!!!")
            continue
        else:
            break

#for loop to get line by execution
    for line in filename:
        gmail_pattern = re.findall('\S+@gmail.com',line)
        if len(gmail_pattern) > 0:
            print(gmail_pattern)

    

gmail_from_file()
