#Tuple ()

a = (1,2,4,3,5,76)

for i in a:
    print(i)

#set
x = set()
a = {"hello",2,2,3,1,5,4,7,89}
print(a)

#dictionary

a = {"name":"john", "age":24, "name": "hello"}
print(a)

a = {i:"value" for i in range(10,20)}
print(a)

b = {i:"even" for i in range(10,20) if i % 2 == 0}
print(b)

c={i:"even" if i%2==0 else "odd" for i in range(10,20)}
print(c)

a = []
for i in range(10,20):
    a.append({i:"value"})
print(a)

#string manipulations

a = "hello world"
x = a[::-1]
x = a[1:-4]
print(x)
