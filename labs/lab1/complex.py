class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Complex(%s, %s)' % (self.real, self.imag)

        # For call to str(). Prints readable form

    def __str__(self):
        if self.imag < 0:
            return '%s - %si' % (self.real, self.imag * (-1))
        else:
            return '%s + %si' % (self.real, self.imag)

            # use the equation: (x1+y1*i) + (x2+y2*i)  = (x1+x2)+(y1+y2)*i

    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __add__(self,other):
        if type(other) == type(self):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real,imag)
        else:
            raise TypeError('TypeError: unsupported operand type')

            # use the equation: (x1+y1*i) - (x2+y2*i)  = (x1-x2)+(y1-y2)*i

    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __sub__(self, other):
        if type(other) == type(self):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)
        else:
            raise TypeError('TypeError: unsupported operand type')

    # use the equation:(x1+y1*i)*(x2+y2*i) = (x1*x2-y1*y2)+(x1*y2+y1*x2)*i
    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __mul__(self, other):
        if not type(other) == type(self):
            raise TypeError('TypeError: unsupported operand type')

        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + other.imag * self.real)

    # use the equation:(x1+y1*i)/(x2+y2*i) = [(x1*x2+y1*y2)+(y1*x2-x1*y2)*i] /(x2*x2+y2*y2)
    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __truediv__(self, other):
        if not type(other) == type(self):
            raise TypeError('TypeError: unsupported operand type')
        real = ( self.real * self.imag + other.real * other.imag ) / (self.imag**2 + other.imag**2)
        imag = (other.real * self.imag - self.real * other.imag) / (self.imag ** 2 + other.imag ** 2)
        return Complex(real, imag)

    def __eq__(self, other):
        if not type(other) == type(self):
            return False

        a = self.real == other.real
        b = self.imag == other.imag
        return a & b