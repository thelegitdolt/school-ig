# memoization!

cache = dict()


def fib_memoize(n):
    if n in cache:
        return cache[n]

    if n <= 1:
        cache[n] = n
        return n
    else:
        cache[n] = fib_memoize(n - 1) + fib_memoize(n - 2)

        return cache[n]


from functools import lru_cache

@lru_cache()
def fib_weird(n):
    if n <= 1:
        return n
    else:
        return fib_weird(n - 1) + fib_weird(n - 2)


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1]

def all_combs(list_, n):
    if n == 0:
        return [[]]
    l = []
    for i in range(0, len(list_)):
        m = list_[i]
        r = list_[i+1:]
        for p in all_combs(r, n - 1):
            l.append([m] + p)

    return l
