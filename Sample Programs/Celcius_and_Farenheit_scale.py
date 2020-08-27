#Scale

#Selecting the Scale
scale = int(input("""
              1. Celcius to Farenheit
              2.Farenheit to celcius
              Your Choice:
             """))
#Celcius to Farenheit Scale
if scale == 1:
    celcius = float(input("Enter the celcius:"))
    farenheit = 0
    farenheit = (celcius * 9 // 5) + 32
    print(f"{farenheit}F")

#Farenheit to Celcius Scale
elif scale == 2:
    farenheit = float(input("Enter the Farenheit:"))
    celcius = 0
    celcius = (farenheit - 32) * 5 // 9
    print(f"{celcius}C")

else:
    print("Choose a Valid Option!!!")
