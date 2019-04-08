class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, pt):
		return Point(self.x + pt.x, self.y + pt.y)

	def __sub__(self, pt):
		return Point(self.x + pt.x, self.y + pt.y)

	def __mul__(self, sc):
		return Point(self.x*sc, self.y*sc)

