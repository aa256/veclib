from collections import namedtuple

class SvgFrame:

	def __init__(self, svgas=[], xmin=0, xmax=None, ymin=0, ymax=None):
		self._svgas = svgas
		self._xmin = xmin
		self._xmax = xmax
		self._ymin = ymin
		self._ymax = ymax

	def add(self, svga):
		self._svgas.append(svga)

	def box(self):
		boxes = [svg.box() for svg in self._svgas]
		(self._xmin, self._ymin, self._xmax, self._ymax) = (min(box[i] for box in boxes) for i in range(4))

	def draw(self):
		self.box()
		out = "<svg viewBox=\"{0} {1} {2} {3}\">\n".format(self._xmin, self._ymin, self._xmax-self._xmin, self._ymax-self._ymin)
		for svga in self._svgas:
			out += "  " + svga.svg() + "\n"
		out += "</svg>"
		return out

	def write_to_html(self, fname):
		out = "<html><body>\n"
		out += self.draw()
		out += "</body></html>"
		f = open(fname, "w")
		f.write(out)
		f.close()