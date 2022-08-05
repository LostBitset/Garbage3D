# (by HktOverload)

from chunks import *
import lighting as l

from generation_geometry import *

# A world of half-cubes
def halfCubeWorld(xCount, yCount):
	return Chunks.generate(
		lambda _: halfCube(),
		2.0, xCount, yCount,
		transform=l.lambertian,
	)

# A flat grid of triangles
# WARNING - If you create more than about 8 triangles per chunk
# it gets really really slow and the PYTHON INTERPRETER ITSELF
# ACTUALLY CRASHES
# I told you this was a sketchy 3D engine
def triGrid(size, count):
	verts = [
		(i*size, j*size, 0) \
			for i in range(count+1) for j in range(count+1)
	]
	tris = []
	for idx, (i, j, _) in enumerate(verts):
		left = idx - 1
		top = idx - count - 1
		diag = top - 1
		if diag < 0 or idx % (count + 1) == 0:
			continue
		tris.append((idx, left, diag))
		tris.append((idx, top, diag))
	return Geom(verts, tris)

# Use Chunks to make a world of tri-grids
# Please read the triGrid documentation
def triGridWorld(xCount, yCount, size, count):
	return Chunks.generate(
		lambda _: triGrid(size, count),
		size*count, xCount, yCount,
		transform=l.lambertian,
	)
