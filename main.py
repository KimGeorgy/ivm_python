from libkim import *
a = tuple((1,2,3))
b = tuple((1,2,3,3,4,5))
x = Vector(3, a)
A = Matrix(2,3,b)
c = A * x
print(c.data)