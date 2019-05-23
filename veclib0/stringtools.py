
def list_of_points(pts):
	out = "\""
	for pt in pts:
		out += "{0},{1} ".format(pt.x, pt.y)
	out += "\""
	return out

