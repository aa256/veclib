from .polygon import Polygon
from .txfn import Txfn

class CircularFlower:
	def __init__(self, n, leaf, rad=100, r=1.61):
		self.n = n
		self.leaf = leaf
		self.r = r

	def expanded(self):
		ngon = Polygon(n, rad_arm=Vec(0, rad))
		rot0 = tx
		leaf = self.leaf*

