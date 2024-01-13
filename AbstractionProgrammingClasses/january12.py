

# data types

# string lists tuples arrays


# FOR ALL ITERABLES:

def main():
    a = [1, 2, 3, 3, 3, 3]

    print(a.count(3))
    # returns 4,  the amount of times 3 shows up in a

    # indexOf? where in a[3:2:5] 3 is
    print(a.index(3, 2, 5))


    # IDENTICAL DICKS
    # Dicks are not ordered.
    a = (dict(one=1, two=2, three=3))
    b = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

    # to remove, use del a['two']

    # SETS
    # difference?
    # disjoint?
    weird = set('hello wassup bitchhhhhh')

    print(weird)



def main_class():
    a = Fraction(3, 4)
    print(a.__str__())
    print(a.__repr__())

    b = Fraction(1, 3)
    print(b)
    print(a * b)



class GoodClass:
    def __init__(self, variable, something_else):
        self.variables = variable
        self.something_else = something_else

    # needs a STRING REPRESENTATION
    def __str__(self):
        return super().__str__()


    def __repr__(self):
        return super().__repr__()


class Fraction:
    def __init__(self, num: int, denom: int):
        self.num = num
        self.denom = denom

    def __str__(self):
        return f'{self.num}/{self.denom}'

    def __repr__(self):
        return f'Fraction({self.num}, {self.denom})'

    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError(f"Cannot add fraction to {type(other)}")

        return Fraction.make_simplified_fraction(self.num * other.denom + other.num * other.denom, self.denom * other.denom)

    def __mul__(self, other):
        if type(other) != type(self):
            raise TypeError(f"Cannot add fraction to {type(other)}")

        return Fraction.make_simplified_fraction(self.num * other.num, self.denom * other.denom)

    def __eq__(self, other):
        a = self.simplify()
        b = other.simplify()
        return a.num == b.num & a.denom == b.denom

    def simplify(self):
        return Fraction.make_simplified_fraction(self.num, self.denom)

    @staticmethod
    def make_simplified_fraction(num:int, denom: int):
        fract_gcd = Fraction.gcd(num, denom)
        return Fraction(int(num / fract_gcd), int(denom / fract_gcd))

    @staticmethod
    def gcd(num1: int, num2: int):
        while num1 % num2 != 0:
            num1, num2 = num2, num1 % num2
        return num2
