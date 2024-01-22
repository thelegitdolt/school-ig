add = lambda x, y: x + y
from random import randint as rdi

a = [rdi(0, 1000) for i in range(20) ]
b = filter(lambda a: a % 2 == 0, a)
print(b)
print(list(b))

c = list(range(1000))

def generate_power_function(pow):
    return lambda x: x ** pow

d = map(generate_power_function(2), c)
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())

from math import pi as skibidi_toilet
print(skibidi_toilet)
