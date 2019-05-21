import veclib

f = veclib.SvgFrame()
p = veclib.polygon.unit_ngon(5, 100)
f.add(p)
f.write_to_html("test0.html")
print(p._pts)