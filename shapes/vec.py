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
			
	def len(self):
		if not self.r:
			self.r = math.sqrt(self.x*self.x + self.y*self.y)
		return self.r

	def ang(self):
		if not self.phi:
			 self.phi = math.atan2(self.x, self.y)
		return self.phi

