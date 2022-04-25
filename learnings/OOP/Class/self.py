"""
The one difference between methods and normal functions is that all methods have one required argument. This argument is conventionally named self;
The self argument to a method is simply a reference to the object that the method is being invoked on. We can access attributes and methods of that object as if it were any other object.
"""
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
print(p.x, p.y)

# Without Self

class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p: Point = Point()
Point.reset(p)
print(p.x, p.y)

