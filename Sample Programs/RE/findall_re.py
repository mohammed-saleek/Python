import re
sentence='''Magesh is 22 ,Lionel is 23,Saleek is 24, and Guhan is 25'''
ages=re.findall(r'\d{1,3}',sentence)
Names=re.findall(r'[A-Z][a-z]*',sentence)
dict={}
x=0
for i in Names:
    dict[i]=ages[x]
    x+=1
print(dict)

