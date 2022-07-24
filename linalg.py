# Kaidun (by HktOverload)

# ZeroVec is a singleton that can be used in the first position of add
# to act as the zero vector (of any length)
# Useful as an initial value when looping (i.e. in mat-vec-mul)

import math

class _ZeroVecT(object):
    def __new__(cls):
        return ZeroVec
    def __copy__(self):
        return ZeroVec
    def __deepcopy__(self):
        return ZeroVec
    def __reduce__(self):
        return (_ZeroVecT, ())

if 'ZeroVec' not in globals():
    ZeroVec = object.__new__(_ZeroVecT)

# Add vectors
def add(a, b):
    if a == ZeroVec:
        return b
    assert len(a) == len(b)
    return [ a[i]+b[i] for i in range(len(a)) ]

# Scale vectors
def sc(a, scalar):
    return [ i * scalar for i in a ]

# Dot product of vectors
def dot(a, b):
    assert len(a) == len(b)
    return sum( a[i]*b[i] for i in range(len(a)) )

# Negate a vector
def neg(a):
    return [ -i for i in a ]

# Normalize a vector
def norm(a):
    return sc(a, 1/math.hypot(*a))

# A matrix with elements stored in column-major order
class Mat(object):
    __slots__ = 'odim', 'idim', 'cols'
    def __init__(self, cols, odim=None, idim=None):
        eps = 10**-6
        cnt = len(cols) 
        if odim == None and idim == None:
            raise Exception('No parts of mat size given')
        elif odim == None:
            if cnt % idim != 0:
                raise Exception(
                    f'Given idim {idim} must be fac of {cnt}'
                )
            else:
                odim = cnt // idim
        elif idim == None:
            if cnt % odim != 0:
                raise Exception(
                    f'Given odim {odim} must be fac of {cnt}'
                )
            else:
                idim = cnt // odim
        else:
            if (odim*idim) != cnt:
                raise Exception(
                    f'No {odim}x{idim} mat has {cnt} elems'
                )
        self.odim, self.idim = odim, idim
        self.cols = cols

    # getting a column
    def col(self, n):
        start = range(0, self.odim*self.idim, self.odim)[n]
        return self.cols[start:start+self.odim]
    
    # getting a row
    def row(self, n):
        return [
            self.cols[i] \
            for i in range(n, self.odim*self.idim, self.odim)
        ]
    
    # transpose
    def t(self):
        return Mat(
            [ j for i in range(self.odim) for j in self.row(i) ],
            odim=self.idim, idim=self.odim,
        )
    
    # mat-vec-mul
    def __mul__(self, v):
        res = ZeroVec
        for i in range(self.idim):
            res = add(res, sc(self.col(i), v[i]))
        return res
    
    # mat-mat-mul
    def __matmul__(self, other):
        assert isinstance(other, self.__class__)
        assert other.odim == self.idim
        resList = []
        for i in range(self.odim):
            for j in range(other.idim):
                resList.append(
                    dot(self.row(i), other.col(j))
                )
        return (self.__class__)(resList, other.idim, self.odim).t()

# Convert into homogenous coordinates
def toH(v):
    return [ *v, 1 ]

# Convert from homogenous coordinates (the perspective divide)
def pDiv(v):
    return [ i/v[-1] for i in v[:-1] ]

# Calculate the cross product in the 3-dimensional case
def cross3(a, b):
    m = Mat([
        0, a[2], -a[1],
        -a[2], 0, a[0],
        a[1], -a[0], 0
    ], 3, 3)
    return m * b
