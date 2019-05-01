class Vec:

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
		if instance(u, Vec):
			return Vec(self.x - u.x, self.y - u.y)
		return NotImplemented

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return Vec(self.x*other, self.y*other)
		elif isinstance(other, Vec):
                  return Vec(self.x * other.x, self.y * other.y)
		return NotImplemented

def __matmul__(self, other):
	return self.x*other.x + self.y*other.y