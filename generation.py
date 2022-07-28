# Kaidun (by HktOverload)

from chunks import *
import lighting as l

from generation_geometry import *

def halfCubeWorld(xCount, yCount):
	return Chunks.generate(
		lambda _: l.lambertian(halfCube()),
		2.0, xCount, yCount
	)
