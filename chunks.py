# Kaidun (by HktOverload)

from geom import *

import rendering as r

def getStdRenderer(dist):
	if dist < 3:
		return r.flat
	else:
		return r.wireframe

class Chunks(object):
	__slots__ = 'indexed', 'xySize', 'rendererFn'
	def __init__(self, indexed, xySize, rendererFn=getStdRenderer):
		self.indexed = indexed
		self.xySize = xySize
		self.rendererFn = rendererFn

	def loaded(self, x, y, chunkDist):
		xIndex, yIndex = x // self.xySize, y // self.xySize
		return [
			self.getChunk(
				xIndex+i, yIndex+j,
				self.hypotXY(i, j)
			) \
				for i in range(-chunkDist, +chunkDist+1)
				for j in range(-chunkDist, +chunkDist+1)
				if self.hasChunk(xIndex+i, yIndex+j)
		]

	def hypotXY(self, cX, cY):
		return math.hypot(cX * self.xySize, cY * self.xySize)

	def getChunk(self, x, y, dist):
		geom = self.indexed[(x, y)]
		return (self.rendererFn)(dist)(geom)

	def hasChunk(self, x, y):
		return (x, y) in self.indexed

	@classmethod
	def generate(cls, gen, xySize, xCount, yCount):
		indexed = {}
		for i in range(xCount):
			for j in range(yCount):
				indexed[(i, j)] = gen((i, j))
		return Chunks(indexed, xySize)
