import numbers

class Vec:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		return self
	
	def __add__(self, other):
		return Vec(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y

	def __neg__(self):
		return Vec(-self.x, -self.y)

	def __sub__(self, other):
		return self + (-other)

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y

	def __mul__(self, other):
		if is_instance(other, numbers.Number):
			return Vec(self.x*other, self.y*other)

	def __div__(self, other):
		if is_instance(other, numbers.Number):
			return Vec(self.x/other, self.y/other)