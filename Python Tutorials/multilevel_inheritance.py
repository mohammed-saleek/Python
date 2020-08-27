from inheritance import Sample

class Show(Sample):
    def show(self):
        print("bye..")

obj = Show(a=20, b=30)
obj.show()
obj.result()
obj.display()
