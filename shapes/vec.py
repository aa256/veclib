import math

class Vec:

	def __init__(self, x, y, r=None, phi=None):
		self.x = x
		self.y = y
		self.r = r
		self.phi = phi

	def from_polar_coords(r, phi):
		return Vec(
			math.cos(angle)*r,
			math.sin(angle)*r,
			r, phi)

	def __add__(self, pt):
		return Point(self.x + pt.x, self.y + pt.y)

	def __sub__(self, pt):
		return Point(self.x + pt.x, self.y + pt.y)

	def __mul__(self, sc):
		return Point(self.x*sc, self.y*sc)

	def len(self):
		if not self.r:
			self.r = math.sqrt(self.x*self.x + self.y*self.y)
		return self.r

	def ang(self):
		if not self.phi:
			 self.phi = math.atan2(self.x, self.y)
		return self.phi

	def within_eps(self, v, eps=0.00001):
		return (self - v).len() < eps

