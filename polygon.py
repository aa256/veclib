import math

from .polyline import Polyline
from .vec import Vec, z


class Polygon(Polyline):

	def __init__(self, n, ctr=z, side_len=None, rad_arm=None, svg_params=None):

		if n < 3:
			return ValueError("Need to specify at least 3 sides.")

		if side_len is None and rad_arm is None:
			raise ValueError("One of side_len and rad_arm needs to be set.")
		if rad_arm is None:
			rad_arm = Vec(0, side_len)

		phi = rad_arm.phi()
		rad = rad_arm.len()
		pts = [
			Vec.by_polar_form(rad, phi + 2 * math.pi * i / n) + z for i in range(n)]
		pts.append(pts[0])
		Polyline.__init__(self, pts, svg_params)
