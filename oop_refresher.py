# %%
class point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

p1 = point()
print("p1 ",p1.x)

p2 = point(2,4)
print("p2 ",p2.x)

print(p2)
# %%
class Shape:
    def __init__(self,points):
        self.points = points

t1 = point(5,5)
t2 = point(10,5)
t3 = point(5,10)
p = [t1,t2,t3]

Shape(p)