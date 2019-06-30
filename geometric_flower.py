from .polyline import Polyline
from .txfn import Txfn

class GeometricFlower:
	def __init__(self, n, unit_leaf, rad=100, r=1.61):
		self.n = n
		self.unit_leaf = unit_leaf
		self.r = r

	def expanded(self):
		phi = Txfn.rotate(n, )

