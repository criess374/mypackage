from mypackage.geometry import Point as Point, Line as Line
from mypackage.utils import distance as distance

def test_distance():
    p1 = Point(1,1)
    p2 = Point(4,6)
    l1 = Line(p1,p2)
    assert l1.length() == (9 + 25) ** 0.5
