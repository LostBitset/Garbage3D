# Kaidun (by HktOverload)

# ZeroVec is a singleton that can be used in the first position of add
# to act as the zero vector (of any length)
# Useful as an initial value when looping (i.e. in mat-vec-mul)

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

# Add vectors (which are actually tuples)
def add(a, b):
    if a == ZeroVec:
        return b
    return ( *( i + j for i in a for j in b ), )

# Scale vectors (which are actually tuples)
def sc(a, scalar):
    return ( *( i * scalar for i in a ), )

# Dot product of vectors (which are actually tuples)
def dot(a, b):
    return sum( i * j for i in a for j in b )

class Mat(object):
    __slots__ = 'odim', 'idim', 'cols'
    def __init__(self, cols, odim=None, idim=None):
        eps = 10**-6
        cnt = len(cols) 
        if odim == None and idim == None:
            raise 'No parts of mat size given'
        elif odim == None:
            if cnt % idim != 0:
                raise f'Given idim {idim} must be fac of {cnt}'
            else:
                odim = cnt // idim
        elif idim == None:
            if cnt % odim != 0:
                raise f'Given odim {odim} must be fac of {cnt}'
            else:
                idim = cnt // odim
        else:
            if (odim*idim) != cnt:
                raise f'No {odim}x{idim} mat has {cnt} elems'
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
            for i in range(n, self.odim*self.idim, self.idim)
        ]
    
    # transpose
    def t(self):
        return Mat(
            [ j for i in range(self.odim) for j in self.row(i) ],
            odim=self.odim, idim=self.idim
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
        resList = []
        for i in range(other.idim):
            for j in range(self.odim):
                resList.append(dot(self.row(i), other.col(j)))
        return (self.__class__)(resList, self.odim, other.idim)

# 3x4 Matrix-vector multiplication
# The matrix should be in column-major order
def mat3x4(mat, v):
    return (
        (v[0]*mat[0]) + (v[1]*mat[3]) + (v[2]*mat[6]) + (v[3]*mat[9]),
        (v[0]*mat[1]) + (v[1]*mat[4]) + (v[2]*mat[7]) + (v[3]*mat[10]),
        (v[0]*mat[2]) + (v[1]*mat[5]) + (v[2]*mat[8]) + (v[3]*mat[11]),
    )

