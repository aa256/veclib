import copy
from ... import veclib

Vec = veclib.base.Vec

pts = [Vec(*p) for p in [(0,0),(200,200),(200,400),(100,500)]]
deltas = [(Vec(*p)) for p in [(0,1),(1,1),(-1,1),(0,1)]]

stem = veclib.base.BezierSpline(pts, deltas)

pentagon = veclib.base.Polygon(5, rad_arm=veclib.base.Vec(0,-100))
z = veclib.base.z
lines = pentagon.lines()
out = []
for line in lines:
	segs = line.n_sect(3)
	p0,p1 = segs[0].a, segs[0].b
	p3,p4 = segs[2].a, segs[2].b
	p2 = z
	out.extend([p0,p1,p2,p3])
out.append(p4)
flower_layer0 = veclib.base.Polyline(out)

print(flower_layer0.pts)

pts = pentagon.pts
p0 = pts[0]

p1 = pts[2] + pts[3]
print(p1)
p1 = p1/2
newlen = (p1 - p0).len()

scale_fac = (newlen-100)/100
print("SCALE_FAC")
print(scale_fac)
r0 = veclib.base.Txfn.rotate(10)
s0 = veclib.base.Txfn.scale(scale_fac)
txfn = r0*s0

layers = [flower_layer0]
flower_layer = flower_layer0
print("TXFN")
print([str(op) for op in txfn.ops])

for i in range(2):
	flower_layer = txfn*flower_layer
	print(flower_layer)
	print([str(pt) for pt in flower_layer.pts])
	layers.append(copy.deepcopy(flower_layer))
s1 = veclib.base.Txfn.scale(1/3)
layers.append(s0*s0*s1*pentagon)
layers.append(stem)

sidelen = 800
params = dict(
	{"viewBox":"{} {} {} {}".format(-sidelen/2, -sidelen/2, sidelen, sidelen)})
frame = veclib.base.SvgFrame(layers, params)
print(frame)
print(frame.svgables)
print(len(frame.svgables))
print(frame.svg_params)
frame.to_html("/Users/andrewarnold/Desktop/foo.html")
