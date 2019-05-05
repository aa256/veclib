import math
from vec import Vec

class Arc(Curve):
	
	_eps = 0.0001

	def __init__(
		self, a=None, b=None, ctr=Vec(0,0), l_vec=None, r_vec=None, phi=None):
		if(a and b and c and l_vec and r_vec):
			if (math.abs(l_vec.len() - r_vec.len() > _eps)):
				raise ValueError("")
			self.a = a
			self.b = b
			self.ctr = ctr
			self.l_vec = l_vec
			self.r_vec = r_vec
			self.phi = phi
			self.r = l_vec.len()

		if(a and b and ctr):
			return Arc.from_end_points(a,b,ctr)

		return Arc.from_vec_arms(ctr, l_vec, r_vec, phi)


	@staticmethod
	def from_end_points(a, b, ctr):
		l_vec=a-ctr
		r_vec=b-ctr
		phi = r_vec.angle() - l_vec.angle()
		return Vec(a, b, ctr, l_vec, r_vec, phi)

	@static method
	def from_vec_arms(ctr, l_vec, r_vec, phi=None):
		check_sum = sum([1 for x in [l_vec, r_vec, phi] if x is not None])
		if check_sum < 2:
			raise ValueError("Need two of l_vec, r_vec, rad")
		if not l_vec:
			l_vec = Vec.from_polar_coords(r_vec.len(), phi-r_vec.angle())
		if not r_vec:
			r_vec = Vec.from_polar_coords(l_vec.len(), phi+l_vec.angle())
		if not phi:
			phi = r_vec.angle() - l_vec.angle() % (2*math.pi)
		a = ctr + l_vec
		b = ctr + r_vec
		return Vec(a, b, ctr, l_vec, r_vec, phi)