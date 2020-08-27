#Bubble Sort

#Creating a list:

list_1 = [2,5,1,10,90,6,12,78,6]
temp = 0
#length = len(list_1)
for count in list_1:
    while list_1[count] > list_1[count+1]:
        temp = list_1[count+1]
        list_1[count+1] = list_1[count]
        list_1[count] = temp

print(list_1)