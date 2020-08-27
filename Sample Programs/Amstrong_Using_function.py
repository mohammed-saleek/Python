#Getting amstrong number using functions

limit = int(input("Enter the starting limit:"))
end = int(input("Enter the end limit:"))

def amstrong(limit,end):
    list_1 = []
    for count in range(limit, end + 1):
        l = len(str(count))
        sum = 0
        temp = count
        while temp > 0:
            rem = temp % 10
            sum += rem ** l
            temp //= 10
        if count == sum:
            list_1.append(count)
    print(list_1)
amstrong(limit,end)