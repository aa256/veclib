
class Mat:
	names = ['a','b','c','d'] 

	def __init__(a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def __add__(self, other):
		return Mat(self.getattr(x)+other.getattr(x) for x in Mat.names)

	def __neg__(self):
		return Mat(-self.getattr(x) for x in Mat.names)

	def __sub__(self, other):
		return self + (-other)

	def __mul__(self, other):
		if isinstance(other, Mat):
			return Mat(
				self.a*other.a + self.b*other.c,
				self.a*other.b + self.b*other.d,
				self.c*other.a + self.d*other.c,
				self.c*other.b + self.d*other.d)
		elif isinstance(other, Vec):
			return Vec(
				self.a*other.a + self.b*other.b, 
				self.c*other.a + self.d*other.b)


