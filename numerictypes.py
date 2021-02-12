from array import array
import math


class Vector:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y, self.z)

    def __abs__(self):
        return math.hypot(self.x, self.y, self.z)

    # By default User defined instances considered true, unless either __boo__ or __len__ is implemented
    def __bool__(self):
        return bool(abs(self))

    # Return result without changing operands
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)


v = Vector(3, 4, 8)


class Vector3d:
    typecode = 'd'

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __iter__(self):
        return (i for i in (self.x,  self.y, self.z))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, [!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return(bytes([ord(self.typecode)])+
               bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y, self.z)

    def __bool__(self):
        return bool(abs(self.x, self.y, self.z))

    



