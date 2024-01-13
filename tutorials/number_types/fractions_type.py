from fractions import Fraction



def run():
    num1, num2, num3, num4 = 125, 21, 30, 16

    # fractions
    frac1 = Fraction(num1, num2)
    frac2 = Fraction(num3, num4)

    print(frac1 / frac2)
