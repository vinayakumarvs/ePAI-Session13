import math

class Polygon:
    def __init__(self, edges: int, circumradius):
        if type(edges) is not int:
            raise TypeError("Edges must be an integer")
        
        if edges < 3:
            raise ValueError("Edges of Polygon must be 3 or greater than 3")

        if type(circumradius) not in [int, float]:
            raise TypeError("circumradius must be either integer or float")


        self._edges = edges
        self._circumradius = circumradius

    @property
    def edges(self):
        return self._edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def vertices(self):
        return self._edges

    @property
    def interior_angle(self):
        return (self.edges - 2) * (180/self.edges)

    @property
    def edge_length(self):
        return 2 * self.circumradius * math.sin(math.pi / self.edges)

    @property
    def apothem(self):
        return self.circumradius * math.cos(math.pi / self.edges)

    @property
    def area(self):
        return 0.5 * self.edges * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self.edges * self.edge_length
    

    def __repr__(self):
        return f"Polygon with \n Edges: {self.edges}, \
                \n Circumradius: {self.circumradius}, \
                \n Interior Angle: {self.interior_angle}, \
                \n Edge Length: {self.edge_length:.2f}, \
                \n Apothem: {self.apothem:.2f}, \
                \n Area: {self.area:.2f}, \
                \n Perimeter: {self.perimeter:.2f}"

    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return (self.edges == other.edges) and (self.circumradius == other.circumradius)
        else:
            raise TypeError("Polygon class instance is expected")

    def __gt__(self, other):
        if isinstance(other,self.__class__):
            return self.vertices > other.vertices
        else:
            raise TypeError("Polygon class instance is expected")
