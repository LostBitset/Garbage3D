# Kaidun (by HktOverload)

class Scene(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def onEvent(cls, app, event):
        # Called when an event occurs
        # These don't use the same format as tkinter
        # For example, pressing 'r' is encoded as ('kb/p', 'r')
        # Moving the mouse to (0, 0) is encoded as ('mouse/to', 0, 0)
        pass

    @classmethod
    def allGeometry(cls, app):
        # A list containing (Geom, Renderer) tuples for everything
        # within this scene
        # Basically just a geomsrc
        # This is not an abstract method because implementing it
        # is optional, not every scene has 3D geometry
        return []

    @classmethod
    def drawOverlay(cls, app, canvas):
    	# A procedure to draw any non-3D elements that go on top
    	# of the 3D part of the scene
    	# This is not an abstractmethod because implementing it
    	# is completely optional
    	pass

# A scene made partially of chunks
class ChunkScene(Scene, abc.ABC):

	@classmethod
	@abc.abstractmethod
	def getLoadedChunks(cls, app):
		# This should return a list of chunks that are to be loaded
		pass

	@classmethod
	def persistentGeometry(cls, app):
		# This should return (Geom, Renderer) tuples for everything
		# that will always be loaded (is not part of a chunk)
		# This is not an abstractmethod because implementing it
		# is optional, not every scene with chunks has this kind of
		# persistent geometry
		return []

	@classmethod
	def allGeometry(cls, app):
		geometry = []
		geometry.extend(cls.persistentGeometry(app))
		geometry.extend([
			chunk.load() for i in cls.getLoadedChunks(app)
		])
		return geometry
