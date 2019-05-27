from .vec import Vec, z

class Polygon(Polyline):

	def __init__(self, n, ctr=z, side_len=None, rad_arm=None):

		if side_len is None and rad_arm is None:
			return ValueError("One of side_len and rad_arm needs to be set.")
		if side_len is not None:
			if rad_arm is None:
				rad_arm = Vec(0, side_len)
			else:
				rad_arm = rad_arm*side_len/rad_arm.len()
		

