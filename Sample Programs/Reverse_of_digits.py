#Reverse of a number
#Get the range using start and end variable

start = int(input("Enter the starting limit:"))
end = int(input("Enter the end Limit:"))

for count in range(start,end):
    rev = str(count)[::-1]
    print(rev)

