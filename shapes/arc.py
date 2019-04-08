
class Arc:
	
	def __init__(
		self, ctr, l_vec=None, r_vec=None, phi=None):

		check_sum = sum([1 for x in [l_vec, r_vec, phi]) 
			if x is None]):
		if check_sum >= 2
			raise ValueError("Need two of l_vec, r_vec, rad");
		
		self.c = ctr
		self.l_vec = ctr + l_vec
		self.r_vec = ctr + r_vec
