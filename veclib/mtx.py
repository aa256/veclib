class Mtx:

	__init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.r0 = None
		self.r1 = None
		self.c0 = None
		self.c1 = None

	__get__(self, col=None, *args):
		if col != None:
			return self[-1-col]
		if len(args==1):
			switch(args[0]):
				case 0:
					return Vec(self.a, self.b)
				case 1:
					return Vec(self.c, self.d)
				case -1:
					return Vec(self.a, self.c)
				case -2:
					return Vec(self.b, self.d)
		elif len(args==2):
			switch(args[0] + 2*args[1]):
				case 0:
					return self.a
				case 1:
					return self.b
				case 2:
					return self.c
				case 3:
					return self.d

	__mul__(self, other):
		return Mtx(
			self[0]*other[-1], self[0]*other[-2],
			self[1]*other[-1], self[0]*other[-2]) 