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

def _diffuseShadingWrapper(viewport, geom=None, f=None, kwargs={}):
    intensities = [ 0.0 ] * len(geom.tris)
    for light in viewport.lighting:
        for i in range(len(geom.tris)):
            intensities[i] += \
                light.intensity(centroid([
                    geom.verts[j] for j in geom.tris[i]
                ]))
    for i in range(len(intensities)):
        intensities[i] = f(
            viewport,
            [ geom.verts[j] for j in geom.tris[i] ],
            intensities[i],
            **kwargs,
        )
    return intensities

def diffuseShadingAlgorithm(f):
    def inner(geom, **kwargs):
        return Geom(
            geom.verts, geom.tris,
            {
                **geom.data,
                'diffuse': functools.partial(
                    _diffuseShadingWrapper,
                    geom=geom, f=f, kwargs=kwargs,
                )
            },
        )
    return inner

@diffuseShadingAlgorithm
def lambertian(viewport, tri, intensity, ambient = 0.1):
    normal = triNormal(tri)
    toCamera = add(viewport.cam.ctr, neg(centroid(tri)))
    toCamera = norm(toCamera)
    return (intensity * abs(dot(normal, toCamera))) + ambient
