# Kaidun (by HktOverload)

from geom import *

class Chunks(object):
	__slots__ = 'indexed', 'xySize'
	def __init__(self, indexed, xySize):
		self.indexed = indexed
		self.xySize = xySize

	def loaded(self, x, y, chunkDist):
		xIndex, yIndex = x // self.xySize, y // self.xySize
		return [
			self.indexed[(xIndex+i, yIndex+j)] \
				for i in range(-chunkDist, +chunkDist+1)
				for j in range(-chunkDist, +chunkDist+1)
		]
