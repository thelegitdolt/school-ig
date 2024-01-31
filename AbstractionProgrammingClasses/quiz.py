def make_dict(string_ls):
    dick = dict()
    for word in string_ls:
        index = len(word) if len(word) < 10 else 10
        the_list = dick.get(index)
        if the_list is None:
            dick[index] = [word]
        else:
            the_list.append(word)

    return dick


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x, self.y})'

    def __add__(self, other):
        if type(other) == type(self):
            return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) == type(self):
            return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point2D(self.x * other, self.y * other)

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        elif not (abs(self.x - other.x) < 0.000001 and abs(self.y - other.y) < 0.000001):
            return False
        else:
            return True

    def distance(self, other):
        from math import sqrt

        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)