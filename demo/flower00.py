import copy
import veclib

pentagon = veclib.Polygon(5, rad_arm=veclib.Vec(0,-100))
z = veclib.z
lines = pentagon.lines()
out = []
for line in lines:
	segs = line.n_sect(3)
	p0,p1 = segs[0].a, segs[0].b
	p3,p4 = segs[2].a, segs[2].b
	p2 = z
	out.extend([p0,p1,p2,p3])
out.append(p4)
flower_layer0 = veclib.Polyline(out)
flower_layer0
pts = pentagon.pts
p0 = pts[0]

p1 = pts[2] + pts[3]
print(p1)
p1 = p1/2
newlen = (p1 - p0).len()

scale_fac = (newlen-100)/100
r0 = veclib.Txfn.rotate(10)
s0 = veclib.Txfn.scale(scale_fac)
txfn = r0*s0
print(s0.mat)

layers = [flower_layer0]
flower_layer = flower_layer0
for i in range(2):
	flower_layer = txfn*flower_layer
	layers.append(copy.deepcopy(flower_layer))
s1 = veclib.Txfn.scale(1/3)
layers.append(s0*s0*s1*pentagon)

sidelen = 1600
params = dict(
	{"viewBox":"{} {} {} {}".format(-sidelen/2, -sidelen/2, sidelen, sidelen)})
frame = veclib.SvgFrame(layers, params)
frame.to_html("/Users/andrewarnold/Desktop/foo.html")