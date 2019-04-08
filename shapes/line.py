class Line():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def mid_pt(self):
		return a+b

	def left_half(self):
		return new Segment(self.a, self.midpoint())

	def right_half(self):
		return new Segment(self.midpoint(), self.b)
