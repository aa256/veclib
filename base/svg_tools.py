
def pts_as_pairs(*pts):
	print(pts)
	out = "points = \""
	for pt in pts:
		print(pt)
		out += "{0},{1} ".format(pt.x, pt.y)
	out += "\" "
	return out

def svg_params(params):
	out = ""

	for k in params.keys():
		out += " " + str(k) + "=\"" + str(params[k]) + "\" "
	return out

defaults = dict()
defaults['stroke']='rgb(0,0,0)'
defaults['stroke-width']=2
defaults['fill']='rgb(255,255,255)'
