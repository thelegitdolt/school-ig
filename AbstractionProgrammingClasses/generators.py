# generators and range function and like, functional programming  I suppose
# and also ranges and iterators and like, all that schnitzels

hi = dict(a=4, b=5, c=6)

a = type(hi)
print(a)

def power_iterator(n):
    a = 0
    while True:
        yield a ** n
        a += 1

def random_number(bound: int):
    from random import randint as rd

    while True:
        yield rd(-bound, bound)


def generator1():
    s = "first"
    yield s

    s = 'second'
    yield s

def char_generator():
    a = 0
    while True:
        yield chr(a)
        a += 1

c = char_generator()

from random import randint as rd



