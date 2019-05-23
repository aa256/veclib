import veclib

f = veclib.SvgFrame()
p = veclib.polygon.unit_ngon(5, 100)
print(p._pts)

def myfun0(line, pt):
	lines = line.n_sect(3)
	return veclib.Polyline([lines[0], Line(lines[1]._a, pt), Line(pt, lines[1]._b), lines[2]])

out = []
for ell in p.lines():
	out.extend(myfun0(ell, veclib.Vec(0,0)))
q = veclib.Polyline(out)
f.add(q)