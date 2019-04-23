import Curve

class Polycurve:
	"""Defines the outline of a 2D shape"""
	def __init__(*args):
		for arg in args:
			if not isinstance(arg, Curve):
				raise ValueE

