class Vector:
    """Represents a vector in a multidimensional space"""

    def __init__(self, d):
        """create d-dimensional vector of zeros"""
        self._coords = [0] * d

    def __len__(self):
        """returns the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """returns the jth element of vector"""
        return self._coords[j]

    def __setitem__(self, j, value):
        """set jth value in the vector"""
        self._coords[j] = value

    def __add__(self, other):
        """returns sum of two vectors"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for key in range(len(self)):
            result[key] = self[key] + other[key]
        return result

    def __eq__(self, other):
        """returns true if vector has same coordinates"""
        return self._coords == other._coords

    def __ne__(self, other):
        "returns true if vectors differ"
        return not self == other

    def __str__(self):
        "productive string  representation of vector"
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == "__main__":

    v1 = Vector(5)
    v2 = Vector(5)
    print(v1 == v2)
    print(v1 + v2)
    print(v1 - v2) #TypeError: unsupported operand type(s) for -: 'Vector' and 'Vector'
    print(v1 > v2) #TypeError: '>' not supported between instances of 'Vector' and 'Vector'
