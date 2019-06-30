from . import svg_tools


class SvgFrame:

	def __init__(self, svgables, svg_params=dict()):
		self.svgables = svgables
		self.svg_params = svg_params

	def to_html(self, fname):
		print("pooooo")
		print(fname)
		outfile = open(fname, "wt")
		outfile.write("<html><body>")
		outfile.write("<svg ")
		outfile.write(svg_tools.svg_params(self.svg_params))
		outfile.write(">")
		for svg in self.svgables:
			outfile.write(svg.svg())
		outfile.write("</svg></body></html>")
		outfile.close()
