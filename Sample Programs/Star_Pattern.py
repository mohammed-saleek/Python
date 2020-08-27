#Star in square

class Patterns:
    def __init__(self):
        self.n = 6
        self.list1 = ["A", "B", "C", "D", "E"]
        self.list2 = [5,4,3,2,1]
        self.list3 = ['E', 'D', 'C', 'B', 'A']

    def star_square(self):
        for i in range (1, self.n):
            for j in range(1, self.n):
                print("*", end=" ")
            print()
        print("\n")

    def number_square(self):
        for i in range(1, self.n):
            for j in range(1, self.n):
                print(i, end=" ")
            print()
        print("\n")

    def number_square_one(self):
        for i in range(1, self.n):
            for j in range(1, self.n):
                print(j, end=" ")
            print()
        print("\n")

    def alphabet(self):
        for i in self.list1:
            for j in self.list1:
                print(i, end=" ")
            print()
        print("\n")

    def square_alphabets(self):
        for i in self.list1:
            for j in self.list1:
                print(j, end=" ")
            print()
        print("\n")

    def number_pyramid(self):
        for i in range(1 , self.n):
            for j in range(1,i+1):
                print(j, end=" ")
            print()
        print("\n")

    def number_square_two(self):
        for i in self.list2:
            for j in self.list2:
                print(j, end=" ")
            print()
        print("\n")

    def rev_alpha_sqr(self):
        for i in self.list3:
            for j in self.list3:
                print(i, end=" ")
            print()
        print("\n")

    def rev_alpha_sqr1(self):
        for i in self.list3:
            for j in self.list3:
                print(j, end=" ")
            print()
        print("\n")

    def ascending_star(self):
        for i in range(1,self.n):
            for j in range(1, i+1):
                print("*",end=" ")
            print()
        print("\n")


obj = Patterns()
obj.star_square()
obj.number_square()
obj.number_square_one()
obj.alphabet()
obj.square_alphabets()
obj.number_pyramid()
obj.number_square_two()
obj.rev_alpha_sqr()
obj.rev_alpha_sqr1()
obj.ascending_star()
