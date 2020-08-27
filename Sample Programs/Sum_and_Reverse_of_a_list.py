#Reverse and sum of list elements

list_1 = [1,20,35,32,47,89,68,74,12,153,13,45]

list_2 =[]
list_3 = []

for elements in list_1:
    rev = 0
    sum = 0
    while elements > 0:
        rev = (rev * 10) + elements % 10
        sum = sum + elements % 10
        elements = elements // 10
    list_2.append(rev)
    list_3.append(sum)
for elements in list_3:
    elements == 
print(list_2)
print(list_3)