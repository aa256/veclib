from .vec import Vec

class Mtx:

	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def __str__(self):
		return "[[%s, %s],[%s,%s]]" % (self.a, self.b, self.c, self.d)

	def __repr__(self):	
		return str(self)

	def __getitem__(self, *args, col=None):
		if col:
			return self[-1-col]
		if len(args) == 1:
			idx = args[0]
			if idx==1:
				return Vec(self.c, self.d)
			elif idx==0:
				return Vec(self.a, self.b)
			elif idx==-1:
				return Vec(self.a, self.c)
			elif idx==-2:
				return Vec(self.b, self.d)
		elif len(args) == 2:
			idx = (args[0], args[1])
			if idx == (0,0):
				return self.a
			elif idx == (0,1):
				return self.b
			elif idx == (1,0):
				return self.c
			elif idx == (1,1):
				return self.d
		raise ValueError("Illegal index fool %s" % idx)

	def __add__(self, mtx):
		return Mtx(
			self.a + mtx.a, self.b + mtx.b,
			self.c + mtx.c, self.d + mtx.d)


	def __mul__(self, other):
		return Mtx(
			self[0]*other[-1], self[0]*other[-2],
			self[1]*other[-1], self[0]*other[-2]) 