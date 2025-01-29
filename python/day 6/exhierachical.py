class shape:
    def area(self):
        pass
        # return 100
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius ** 2
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side * self.side
c=circle(4)
s=square(5)
print("area of the circle is",c.area())
print("area of the square is ",s.area())
# sh=shape()
# print(sh.area())
