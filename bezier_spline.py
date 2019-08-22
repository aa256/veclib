from . import svg_tools

class BezierSpline(Svgable, ):

    def __init__(self, pts, rel_ctrl_pts):
        """
        pts: list of vecs
        rel_ctrl_pts:
            the parameterized derivative at each point, relative to
            the length of each segment.
        """
        self.pts = pts
        self.rel_ctrl_pts = rel_ctrl_pts

    def svg():
        idx = 0
        out = "<M = {}".format(svg_tools.pts_as_pairs())
