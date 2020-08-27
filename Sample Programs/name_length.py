#Checking Name length

name = input("Enter Your Name:")
length_of_name = len(name)

#checking length of the name
if length_of_name < 3:
    print("Name Must be at least three characters!!! ")
elif length_of_name > 50:
    print("Name can be a maximum of 50 characters!!!")
else:
    print("Name looks good")