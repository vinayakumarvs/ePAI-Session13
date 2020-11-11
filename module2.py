from module1 import Polygon
from functools import lru_cache

class PolygonSeq():
    def __init__(self, edges, circumradius):
        if type(edges) is not int:
            raise TypeError("Edges must be an integer")
        
        if edges < 3:
            raise ValueError("Edges of Polygon must be 3 or greater than 3")

        if type(circumradius) not in [int, float]:
            raise TypeError("circumradius must be either integer or float")

        self._edges = edges
        self._circumradius = circumradius
        PolygonSeq._circumradius = circumradius

    def __len__(self):
        return self._edges - 2

    def __getitem__(self, i):
        if isinstance(i, int):
            if i < 0:
                i = self._edges - 2 + i
            if i < 0 or i >= (self._edges - 2):
                raise IndexError
            else:
                return PolygonSeq._newpoly(i)
        else:
            start, stop, step = i.indices(self._edges - 2)
            diff = range(start, stop, step)
            return [PolygonSeq._newpoly(j) for j in diff]

    @staticmethod
    @lru_cache(2**10)
    def _newpoly(n):
        return Polygon(n + 3, PolygonSeq._circumradius)

    @property
    @lru_cache(1)
    def max_effi_polygon(self):
        return sorted(self, key=lambda x:x.area / x.perimeter, reverse =True)[0]
    
    def __repr__(self):
        return f"{tuple(self)}"

    
