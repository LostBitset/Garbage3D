# Kaidun (by HktOverload)

import abc, math, functools

from geom import *

# The top-level functions should not be imported using star
__all__ = 'Light PointLight'.split()

class Light(abc.ABC):

    @abc.abstractmethod
    def intensity(self, target):
        pass

class PointLight(Light):
    def __init__(self, ctr, brightness):
        self.ctr = ctr
        self.brightness = brightness
    
    def intensity(self, target):
        dist = math.hypot(*add(target, neg(self.ctr)))
        return self.brightness * (1 / (dist ** 2)) # inv-square law

def _diffuseShadingWrapper(lighting, geom=None, algorithm=None):
    intensities = [ 0.0 ] * len(geom.tris)
    for light in lighting:
        for i in range(len(geom.tris)):
            intensities[i] += \
                light.intensity(centroid([
                    geom.verts[j] for j in geom.tris[i]
                ]))
    for i in range(len(intensities)):
        intensities[i] = algorithm(geom.tris[i], intensities[i])
    return intensities

def diffuseShadingAlgorithm(f):
    def inner(geom):
        return Geom(
            geom.verts, geom.tris,
            {
                **geom.data,
                'diffuse': functools.partial(
                    _diffuseShadingWrapper, geom=geom, algorithm=f,
                )
            },
        )
    return inner

@diffuseShadingAlgorithm
def lambertian(tri, intensity):
    return intensity # TODO actual lambertian reflectance
