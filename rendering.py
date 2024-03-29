# (by HktOverload)

from geom import *

# Do not import * from this, it will bring only confusion
# This defines rendering-specific top-level functions
# Instead, use the following:
# import rendering as r
__all__ = '__no_star_import__',
__no_star_import__ = True

# A renderer is simply a function of the type
# (Viewport, Canvas, List3[Coord2], Dict[Str,Any]) -> NoneType
# It draws the given tri on the given canvas as the given viewport
# sees it
# However, a renderer ref is usually accompanied by the target geometry
# These are the (Geom, Renderer) pairs
# To make this easier, the rendering functions take geometry and return
# these pairs
# The decorated version of the function also takes something that
# yields transformations that take the same arguments as it does,
# except for the canvas and any kwargs, which it applies to the tris,
# and return (tri, newKwargs) pairs
# This is done with the @renders decorator
def renders(renderer, **kwargs):
    def inner(geom, chain=[]):
        def sub(viewport, canvas, tri, idx, data, **kwargs2):
            kwargs.update(kwargs2)
            for f in chain:
                tri, newKwargs = f(viewport, tri, idx, data)
                if newKwargs != None:
                    kwargs.update(newKwargs)
            return renderer(
                viewport, canvas, tri, idx, data, **kwargs
            )
        return geom, sub
    return inner

def toScreenSpace(viewport, tri):
        sX, sY = viewport.pxSize[0]//2, viewport.pxSize[1]//2
        return [
            j for i in tri for j in (
                int(i[0] * sX + sX),
                int(i[1] * sY + sY)
            )
        ]

@renders
def wireframe(viewport, canvas, tri, idx, data, color='blue'):
    if data != None and 'wireframe-color' in data:
        newColor = data['wireframe-color'][idx]
        if newColor != None:
            color = newColor
    canvas.create_polygon(
        *toScreenSpace(viewport, tri),
        fill='', outline=color,
    )

def clamp(x):
    return min(1.0, max(0.0, x))

@renders
def flat(viewport, canvas, tri, idx, data):
    assert data != None and 'diffuse' in data
    intensity = data['diffuse'](viewport)[idx]
    adj = int(clamp(1-intensity) * 255)
    color = data['color'][idx] if 'color' in data else 0xFFFFFF
    r, g, b = (color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF
    r, g, b = max(0, r - adj), max(0, g - adj), max(0, b - adj)
    canvas.create_polygon(
        *toScreenSpace(viewport, tri),
        fill=f'#{r:02x}{g:02x}{b:02x}', width=0,
    )
