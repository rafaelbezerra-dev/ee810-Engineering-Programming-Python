import math

def simpleFunction(x):
    return x + 4

L = lambda x: x + 4

print L(4)
print simpleFunction(4)

L = lambda x, y: x + y
print L(2,3)

L = [lambda x: x**2,
    lambda x: x**3,
    lambda x: x**4]

for item in L:
    print item(2)

def funpowers(n):
    return lambda x: math.pow(n, x)

pow2 = funpowers(2)
pow3 = funpowers(3)

print pow2(3)
print pow3(2)
