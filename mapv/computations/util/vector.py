import math

class Vector():

    def __init__(self, mode, v1, v2):

        if mode == 'radians':
            self.x = math.cos(math.radians(v2)) * v1
            self.y = math.sin(math.radians(v2)) * v1
        elif mode == 'directions':
            self.x = v1
            self.y = v2
        else:
            raise TypeError(f'Unknown vector type "{mode}"')

    def __repr__(self):
        return f'<mapv.computations.Vector({self.x}, {self.y})>'