
def points_str(pts):
	out = "\""
	for pt in pts:
		out += "{0},{1} ".format(pt.x, pt.y)
	out += "\""
	return out

def params_str(params):
	out = ""
	for k in params.keys():
		out += str(k) + " = " + str(params[k]) + " "
	return out

defaults = dict()
defaults['stroke']='rgb(255,0,0)'
defaults['stroke-width']=2
