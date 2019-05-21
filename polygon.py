import math
import typing

from .polyline import Polyline
from .vec import Vec 

def unit_ngon(n: int, side: float=10.0):
	if n < 3:
		return ValueError("Need at least 3 points to make a polygon.")
	pts = [Vec(side*math.sin(2*math.pi*i/n), -side*math.cos(2*math.pi*i/n)) for i in range(n)]
	for pt in pts:
		print(pt)
	pts.append(Vec(0, -side))
	return Polyline(*pts)

