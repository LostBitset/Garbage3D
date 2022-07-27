# Kaidun (by HktOverload)

from geom import *

class Chunks(object):
	__slots__ = 'indexed', 'size'
	def __init__(self, size):
		self.indexed = {}
		self.size = size
