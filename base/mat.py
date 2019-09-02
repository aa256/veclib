import numbers

from .vec import Vec


class Mat:
	names = ['a', 'b', 'c', 'd']

	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def __str__(self):
		return "[[{},{}],[{},{}]]".format(self.a, self.b, self.c, self.d)

	def __add__(self, other):
		return Mat(self.getattr(x) + other.getattr(x) for x in Mat.names)

	def __neg__(self):
		return Mat(-self.getattr(x) for x in Mat.names)

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if isinstance(other, Mat):
			return Mat(
				self.a * other.a + self.b * other.c,
				self.a * other.b + self.b * other.d,
				self.c * other.a + self.d * other.c,
				self.c * other.b + self.d * other.d)
		elif isinstance(other, Vec):
			return Vec(
				self.a * other.x + self.b * other.y,
				self.c * other.x + self.d * other.y)
		elif isinstance(other, numbers.real):
			return Mat(self.a*other, self.b*other, self.c*other, self.d*other)

	def __invert__(self):
		if self.a*self.d == self.b*self.c:
			return ArithmeticError("Matrix {} is not invertible".format())
		return 1/(self.a*self.d - self.b*self.c)

	@classmethod
	def I(cls):
		return Mat(1,0,0,1)
		
I = Mat(1, 0, 0, 1)