#Sum of Elements of the List


sum = 0
sum_of_elements = []
list_elements = [10,11,12,13,14,15,16,17,18,19,20]
for number in list_elements:
    while (number > 0):
        reminder = number % 10
        sum = sum + reminder
        number = number // 10
sum_of_elements.append(number)
print(sum_of_elements)