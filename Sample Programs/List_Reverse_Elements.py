#Reversing List Elements

'''list_1 = [elements for elements in range(20,30)]
reverse = 0
reversed_list = []
for count in list_1:
    while(count != 0):
        digit = count * 10
        reverse = reverse * 10 + digit
        count = count // 10
    reversed_list.append(count)

print(list_1)
print(reversed_list)
'''
#Reverse of Elements of the list
#Get the range using start and end variable

start = int(input("Enter the starting limit:"))
end = int(input("Enter the end Limit:"))
reversed_list = []
for count in range(start,end):
   # rev = str(count)[::-1]
    reversed_list.append(str(count)[::-1])
print(reversed_list)

