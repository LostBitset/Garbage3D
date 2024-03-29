# (by HktOverload)

from geom import *

import rendering as r

# Get a renderer to use based on the distance away
# This lets you use realistic but computationally intense
# renderers only for geometry close to the camera
def getStdRenderer(dist):
	if dist < 3:
		return r.flat
	else:
		return r.wireframe

# A class that represents a sequence of chunks
class Chunks(object):
    # indexed <-> A dictionary mapping (x, y) pairs to chunks
    # xySize <-> The size of each chunk
    # transform <-> An optional transformation applied to the
    #               geometry before rendering
    # rendererFn <-> See documentation for getStdRenderer (which
    #                is the default value for this)
	__slots__ = 'indexed', 'xySize', 'transform', 'rendererFn'
	def __init__(
		self, indexed, xySize,
		transform=None, rendererFn=getStdRenderer,
	):
		self.indexed = indexed
		self.xySize = xySize
		self.transform = transform
		self.rendererFn = rendererFn

    # Return a list of all loaded chunks
    # This returns a list of geometry to which the renderer
    # has already been applied
	def loaded(self, x, y, chunkDist):
		xIndex, yIndex = x // self.xySize, y // self.xySize
		return [
			self.getChunk(
				xIndex+i, yIndex+j,
				self.hypotXY(i, j)
			) \
				for i in range(-chunkDist, +chunkDist+2)
				for j in range(-chunkDist, +chunkDist+2)
				if self.hasChunk(xIndex+i, yIndex+j)
		]

    # A version of math.hypot for xy-coords that refer to chunks
	def hypotXY(self, cX, cY):
		return math.hypot(cX * self.xySize, cY * self.xySize)

    # Get a (rendered) chunk
	def getChunk(self, x, y, dist):
		geom = self.indexed[(x, y)]
		deltaX, deltaY = self.xySize * x, self.xySize * y
		geom = geom.translated([deltaX, deltaY, 0])
		if self.transform != None:
			geom = (self.transform)(geom)
		return (self.rendererFn)(dist)(geom)

    # Check if a chunk exists
	def hasChunk(self, x, y):
		return (x, y) in self.indexed

    # A useful factory method to generate chunks using some
    # procedural generation algorithm passed in as the gen
    # parameter
	@classmethod
	def generate(cls, gen, xySize, xCount, yCount, **kwargs):
		indexed = {}
		for i in range(xCount):
			for j in range(yCount):
				indexed[(i, j)] = gen((i, j))
		return Chunks(indexed, xySize, **kwargs)
