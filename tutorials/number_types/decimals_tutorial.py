from decimal import *

def run():
    num1, num2, num3, num4 = 125, 21, 30, 16

    # decimal numbers
    print(num1 / num2)

    getcontext().prec = 3

    dec1 = Decimal(num3)/Decimal(num4)
    print(dec1)