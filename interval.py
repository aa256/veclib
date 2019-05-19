class Interval():
	def __init__(self, a, b):
		if a > b:
			(a,b) = (b,a)
		self.a = a
		self.b = b

	def a(self):
		return self.a

	def b(self):
		return self.b