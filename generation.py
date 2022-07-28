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

def triGrid(size, count):
	verts = [
		(i*size, j*size, 0) \
			for i in range(count+1) for j in range(count+1)
	]
	tris = []
	for idx, (i, j, _) in enumerate(verts):
		if (i | j) == 0: continue
		left = idx - 1
		top = idx - count - 1
		diag = top - 1
		tris.append((idx, left, diag))
		tris.append((idx, top, diag))
	return Geom(verts, tris)

def triGridWorld(xCount, yCount, size, count):
	return Chunks.generate(
		lambda _: triGrid(size, count),
		size*count, xCount, yCount,
		transform=l.lambertian,
	)
