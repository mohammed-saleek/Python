"""print("hello world")

#int, float, str, bool,complex


a = 12
print(type(a))

b = 23.4
print(type(b))

c='hello'
print(type(c))

d = True
print(type(d))

e = 2 + 3j
print(type(e))


Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
     
    Reverse = (Reverse *10) + Number %10    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)   


Reverse = 0
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    Number = int(input('Enter number '))
    lst.append(Number)    
while lst >0:
     
        Reverse = (Reverse *10) + lst %10    
        lst = lst //10    
     
print("\n Reverse of entered number is = %d" %Reverse)   


"""
list = []

    #Import 20 random numbers
for i in range(0,20):
    list.append(i)
print (i)

rev=0
while list>0:
    rev=(rev*10)+list%10
    list//=10
    print(list)
    
    

