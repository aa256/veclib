from . import SvgAble
from collections import namedtuple

class SvgFrame:



	__init__(self, xmin=0, xmax=None, ymin=0, ymax=None, *svgas, **svg_dict):
		self._svgas = dict()
		for idx, svga in svgas:
			self._svgas[idx]
		self._rect = 
		self._xmin = xmin
		self._xmax = xmax
		self._ymin = ymin
		self._ymax = ymax

	def set_boundary(self):


	def get_min_outer_rect(self):
		xmin = math.Inf
		xmax = -math.Inf
		ymin = math.Inf
		ymax = -math.Inf



	def draw_frame():
		out = "<svg height=\"{0}\" width=\"{1}\">\n".format(self._ht, self._wd)
		for svga in self._svgas
			out += "  " + svga.svg() + "\n"
		out += "</svg>"
		return out
