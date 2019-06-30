from .txfn import Txfn


class GeometricFlower:
	"""Class for generating 2D radial flowers"""

	def __init__(self, n, ell, seed_leaf, r=1.61):
		"""
		n: number of leaves per layer
		ell: number of layers
		seed_leaf: Polyline represeting leaf in first layer. Pointing vertically and originating at origin.
		r: radial geometric growth rate per layer
		"""
		self.n = n
		self.seed_leaf = seed_leaf
		self.r = r

	def expanded(self, ell):
		phi = Txfn.rotate(2*self.n)
		phi2 = phi*phi
		root_leaf = self.seed_leaf
		out = []
		scale = Txfn.scale(self.r)

		for i in range(self.ell):
			leaf = root_leaf
			for j in range(self.n):
				out.append(leaf)
				leaf = phi2*leaf
			root_leaf = scale*root_leaf
		return out
