from libkim import *

eps = 0.00001
alpha = -0.01

input_b = tuple((2,-2,0))
input_A = tuple((3,1,3,1,1,1,2,1,3))
b = Vector(len(input_b), input_b)
A = Matrix(3,3,input_A)

x = Vector(b.size, b.data)

counter = 0
res = 1
while res > eps and counter < 10000:
    r = (A * x - b) * alpha
    res = abs(r)
    x = x + r
    counter += 1

print(f'Resudual: {res}')
print(f'Iterations: {counter}')

print(x.data)