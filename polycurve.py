



class Polycurve:

	def __init__(self, *curves):
		self.curves = list(*curves)

	def transform(self, txfn):
		return Polycurve(txfn*curve for curve in self.curves)

	def to_svg(self):
