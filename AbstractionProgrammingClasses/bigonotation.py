from time import time



def keep_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(args, kwargs)
        end = time()
        return start - end
    return wrapper

@keep_time
def sum1(n: int):
    result = 0
    for i in range(1, n+1):
        result += i
    return result

@keep_time
def sum2(n):
    result = int((n * (n+1))/ 2)
    return result


# how to actaully do it
# WE CAN HAVE DIFFERENT RESULTS AND DIFFERENT ALGORITHMS HAVE DIFFERENET EFFICIENCIES
# CONCATANATIOn

@keep_time
def test1():
    l = []
    for i in range(100):
        l += [i]
    return l

@keep_time
def test2():
    l = []
    for i in range(1000):
        l.append(i)
    return l

@keep_time
def test3():
    return [i for i in range(1000)]

@keep_time
def test4():
    return list(range(1000))


