#Sum of numbers

number = int(input("Enter a number:"))
sum = 0
#while condition
while (number > 0):
    reminder = number % 10
    sum = sum + reminder
    number = number // 10

print("The sum of digits are:",sum)