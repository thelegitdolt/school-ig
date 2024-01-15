def require_two_identical_types(func):
    def check(self, other):
        if not type(other) == type(self):
            raise TypeError('TypeError: unsupported operand type')
        a = func(self, other)
        return a
    return check

from math import sqrt, cos, asin

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001

    @require_two_identical_types
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    @require_two_identical_types
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, scalar):

        return Vector2D(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar == 0:
            return None

        return Vector2D(self.x / scalar, self.y / scalar)

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if not type(self) == type(other):
            return False

        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    @require_two_identical_types
    def __ge__(self, other):
        return float.__ge__(self.magnitude(), other.magnitude())

    @require_two_identical_types
    def __le__(self, other):
        return float.__le__(self.magnitude(), other.magnitude())

    @require_two_identical_types
    def __lt__(self, other):
        return float.__lt__(self.magnitude(), other.magnitude())

    @require_two_identical_types
    def __gt__(self, other):
        return float.__gt__(self.magnitude(), other.magnitude())

    def __hash__(self):
        return id(self)

    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

    def __repr__(self):
        return 'Vector2D(%s, %s)' % (self.x, self.y)

    def magnitude_squared(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return sqrt(self.magnitude_squared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return Vector2D(self.x / self.magnitude(), self.y / self.magnitude())
        return None

    @require_two_identical_types
    def something(self, other):
        self_angle = asin(self.y / self.magnitude())
        other_angle = asin(other.y / other.magnitude())
        return self.magnitude() * cos(self_angle - other_angle)

    @require_two_identical_types
    def dot(self, other):
        return self.x * other.x + other.y * self.y

    def copy(self):
        return Vector2D(self.x, self.y)