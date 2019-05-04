class Vec:

	Z = Vec(0,0)

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "[%s %s]^T" % (self.x, self.y)

	def __repr__(self):	
		return str(self)

	def __add__(self, u):
		if isinstance(u, Vec):
			return Vec(self.x + u.x, self.y + u.y)
		return NotImplemented

	def __sub__(self, u):
		if isinstance(u, Vec):
			return Vec(self.x - u.x, self.y - u.y)
		return NotImplemented

	def __neg__(self, u):
		return Vec(-self.x, -self.y)

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return Vec(self.x*other, self.y*other)
		elif isinstance(other, Vec):
            return self.x*other.x + self.y*other.y
		return NotImplemented

	def __rmul__(self, other):
		return self*other

	def __imul__(self, other):
		if isinstance(other, (int, float)):
			self.x *= other
			self.y *= other
			return self