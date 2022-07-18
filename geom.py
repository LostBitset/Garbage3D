# Kaidun (by HktOverload)

from collections import namedtuple

# A geometry
Geom = namedtuple('Geom', ('verts', 'tris', 'aabb'))

# A camera
Cam = namedtuple('Cam', ('ctr', 'size', 'flen'))

# Convert to the camera's coordinate space
def camcoorder(cam, x):
    a, b, c = cam.ctr
    x, y, z = x
    return (x-a, y-b, c-z)

# 3x3 Matrix-vector multiplication
# The matrix should be in column-major order
def mat3x3(mat, x): 
    return (
        (x[0]*mat[0]) + (x[1]*mat[3]) + (x[2]*mat[6]),
        (x[0]*mat[1]) + (x[1]*mat[4]) + (x[2]*mat[7]),
        (x[0]*mat[2]) + (x[1]*mat[5]) + (x[2]*mat[8]),
    )

# Scaling an n-dimensional vector
def scale(x, scalar):
    return ( *( i*scalar for i in x ), )

# Perform a complete perspective transform
def persp(cam, x):
    x, y, z = camcoorder(cam, x)
    return scale(
        (
            x / (z*cam.size[0]),
            y / (z*cam.size[1]),
        ),
        cam.flen,
    )
