from ..svg import svg_tools
from ..svg.svgable import Svgable
from .txable import Txable

class BezierSpline(Svgable, Txable):

    def __init__(self, pts, dpts):
        """
        pts: list of vecs
        rel_ctrl_pts:
            the parameterized derivative at each point, relative to
            the length of each segment.
        """
        self.pts = pts
        self.dpts = dpts
        self.n = len(self.pts)
        if len(dpts) != self.n:
            raise ValueError(
            "BezierSpline requires the same number of points and derivatives.")

        p = self.pts[0]
        dp = self.dpts[0]
        dp = dp/dp.len()
        self.shift = p
        self.triples = []
        for i in range(self.n-1):
            q = self.pts[i+1]
            dq = self.dpts[i+1]
            dq = dq/dq.len()
            dist = (p-q).len()
            self.triples.append((p+(dp*dist/2), q-(dq*dist/2), q))
            p = q
            dp = dq

    def svg(self):
        idx = 0
        p = self.shift
        out = "<path d=\"M {} {} ".format(p.x, p.y)

        for trip in self.triples:
            out += "C {},{} {},{} {},{} ".format(
            trip[0].x, trip[0].y, trip[1].x, trip[1].y, trip[2].x, trip[2].y)
        out += "\" fill=\"None\" stroke=\"black\"\>"
        return out
