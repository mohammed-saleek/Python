import turtle

class MiddleFinger:
    def __init__(self):
        self.t = turtle.Turtle()

    def mid_fing(self):
        self.t.right(-90)
        self.t.forward(210)
        self.t.right(90)
        self.t.forward(30)
        self.t.right(90)
        self.t.forward(100)
        #first finger ends
        self.t.right(180)
        self.t.forward(100)
        self.t.right(90)
        self.t.forward(30)
        self.t.right(90)
        self.t.forward(100)
        #from second end
        self.t.right(180)
        self.t.forward(200)
        self.t.right(90)
        self.t.forward(30)
        self.t.right(90)
        self.t.forward(200)
        #thi
        self.t.right(180)
        self.t.forward(100)
        self.t.right(90)
        self.t.forward(30)
        self.t.right(90)
        self.t.forward(150)
        #fou
        self.t.right(-150)
        self.t.forward(70)
        self.t.right(90)
        self.t.forward(30)
        self.t.right(90)
        self.t.forward(70)
        self.t.right(330)
        self.t.forward(50)
        # attach
        self.t.right(90)
        self.t.forward(150)




obj = MiddleFinger()
obj.mid_fing()
