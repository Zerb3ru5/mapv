class Point:
    '''
    A `Point`stores a position in space and holds therewith up to 3 coordinates.

    ...

    Attributes
    ----------
    x : float
        stores the x coordinate
    y : float, optional
        stores the y coordinate, defaults to 0
    z : float, optional
        stores the z coordinate, defaults to 0
    dimension : int, optional
        defines the dimenion of the point (how many coordinates it has), defaults to 1
    '''

    def __init__(self, x, y=0.0, z=0.0, dimension=1):

        self.dimension = dimension

        if dimension == 3:
            self.x = x
            self.y = y
            self.z = z
        elif dimension == 2:
            self.x = x
            self.y = y
        else:
            self.x = x


    def __repr__(self):
        if self.dimension == 3:
            return f"<{self.x}, {self.y}, {self.z}>"
        elif self.dimension == 2:
            return f"<{self.x}, {self.y}>"
        else:
            return f"<{self.x}>"