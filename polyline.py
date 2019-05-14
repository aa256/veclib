from .line import line

class PolyLine:

	def __init__(self, lines*):
		ell = len(lines)
		if ell < 3:
			return ValueError("Require at least 3 lines")
		for i in range(1, ell):
			prev = lines[i-1]
			curr = lines[i]
			if lines[i-1]


