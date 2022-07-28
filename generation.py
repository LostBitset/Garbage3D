# Kaidun (by HktOverload)

from chunks import *
import lighting as l

from generation_geometry import *

def halfCubeWorld(xCount, yCount):
	return Chunks.generate(
		lambda _: halfCube(),
		2.0, xCount, yCount,
		transform=l.lambertian,
	)
