from .vec import Vec

class Mtx:

	def __init__(self, a, b, c, d):
		self._a = a
		self._b = b
		self._c = c
		self._d = d

	def __str__(self):
		return "[[%s, %s],[%s,%s]]" % (self._a, self._b, self._c, self._d)

	def __repr__(self):	
		return str(self)

	def __getitem__(self, *args, col=None):
		if col:
			return self[-1-col]
		if len(args) == 1:
			idx = args[0]
			if idx==1:
				return Vec(self._c, self._d)
			elif idx==0:
				return Vec(self._a, self._b)
			elif idx==-1:
				return Vec(self._a, self._c)
			elif idx==-2:
				return Vec(self._b, self._d)
		elif len(args) == 2:
			idx = (args[0], args[1])
			if idx == (0,0):
				return self._a
			elif idx == (0,1):
				return self._b
			elif idx == (1,0):
				return self._c
			elif idx == (1,1):
				return self._d
		raise ValueError("Illegal index fool %s" % idx)

	def __add__(self, mtx):
		return Mtx(
			self._a + mtx._a, self._b + mtx._b,
			self._c + mtx._c, self._d + mtx._d)

	def __neg__(self):
		return Mtx(-self._a, -self._b, -self._c, -self._d)

	def __mul__(self, other):
		if isintance(other, Mtx):
			return Mtx(
				self[0]*other[-1], self[0]*other[-2],
				self[1]*other[-1], self[1]*other[-2]) 			
		elif isinstance(other, Vec):
			return Vec(self[0]*other, self[1]*other)
		elif isinstance(other, (int, float)):
			return Mtx(self._a*other, self._b*other, self._c*other, self._d*other)

	def __rmul__(self, other):
		return other*self

	def __inv__(self):
		disc = self._a*self._d - self._b*self._c
		if disc == 0:
			return ValueError("Non-invertible matrix %s" % str(self))
		return (1/disc)*Mtx(d, -b, -c, a)

	def a(self):
		return self._a

	def b(self):
		return self._b

	def c(self):
		return self._c

	def d(self):
		return self._d

I = Mtx(1,0,0,1)
