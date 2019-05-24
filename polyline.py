
class Polyline(Atom):

	svg_prefix = "<polyline "
	svg_suffix = "/>"

	def __init__(self, pts):
		self.pts = pts

	def vecs(self):
		return self.pts

	def params(self):
		return dict()

