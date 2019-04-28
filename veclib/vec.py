class Vec:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, u):
		return Vec(self.x + u.x, self.y + u.y)

	def __sub__(self, u):
		return Vec(self.x - u.x, self.y - u.y)

	def __mul__(self, other):
		return self.x * other.x + self.y * other.y