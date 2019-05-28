from .polyline import Polyline
from .vec import Vec, z

class Polygon(Polyline):

	def __init__(self, n, ctr=z, side_len=None, rad_arm=None):

		if n < 3:
			return ValueError("Need to specify at least 3 sides.")

		if side_len is None and rad_arm is None:
			return ValueError("One of side_len and rad_arm needs to be set.")
		if rad_arm is None:
			rad_arm = Vec(0, side_len)
		elif side_len is None:
			rad_arm = rad_arm*side_len/rad_arm.len()

		phi = rad_arm.phi()
		rad = rad_arm.len()
		pts = [Vec.by_polar_coords(rad, phi + 2*math.pi*i/n)+z for i in range(n)]
		pts.append(vec[0])

		Polyline.__init__(self, pts)

