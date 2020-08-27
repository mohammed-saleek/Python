#list  []

a = [10,1,2,3,4.5,'hello']
print(a)
x = []
for i in range(10,20):
    x.append(i)
print(x)

y = []
z = []
for i in x:
    if i % 2 == 0:
        y.append(i)
    else:
        z.append(i)
print(y,z)

#list comperhension

x = [i for i in range(10,20)]
print(x)

y = [i for i in range(10,30) if i % 2 == 0]
print(y)

z = [i if i % 2 == 0 else "odd" for i in range(10,20)]
print(z)

z[3] = "bye"
print(z)
