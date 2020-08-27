class Sample:
    a = 0
    def __init__(self, a):
        self.a = a

    def odd_even(self):
        if self.a % 2 == 0:
            print(f"{self.a} is the even number")

    def __del__(self):
        print("bye..")

obj = Sample(a=34)
print(id(obj))
obj.odd_even()
del obj
