class Line(Curve):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def rho_point(self):
		return a*rho + b*(1-rho)

	def mid_pt(self):
		return self.rho_point(a,b)

	def fraction(self, n, ell, arr):
		return Line(rho_point(ell/n), rho_point(arr/n))

	def left_half(self):
		return self.fraction(2, 0, 1)

	def right_half(self):
		return self.fraction(2, 1, 0)
