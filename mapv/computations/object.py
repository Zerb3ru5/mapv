import math
from copy import copy

class Object:
    '''
    A `Object` stores the information of one specific object in the simulation. 
    It tracks also the time-dependent properties the object has on any timestep accessible 
    in the simulation

    ...

    Attributes
    ----------
    obj_prop : dict
        a dictionary that contains all the initial information about the object
    dimension : int, optional
        the number of dimensions the object has / is in

    Methods
    -------
    add_timestep(velocity, position):
        appends a new timestep to the objects timeframe
    '''

    velocity = []
    position = []

    def __init__(self, obj_prop, dimension=1):

        # the description of the shape
        self.name = obj_prop['name']
        self.shape = obj_prop['shape']
        self.color = obj_prop['color']

        # the static properties
        self.dimension = dimension
        self.mass = obj_prop['mass']
        self.acceleration = obj_prop['acceleration']

        # the time-dependent properties
        self.velocity.append(obj_prop['velocity'])
        self.position.append(obj_prop['position'])


    def add_timestep(self, velocity, position):
        '''
        Add a new timestep to the objects timeframe. 

        Paratemers
        ----------
        velocity : float
            the new velocity of the object
        position : Point
            the new position of the object

        Returns
        -------
        None
        '''
        self.velocity.append(velocity)
        self.position.append(position)


    def copy(self):
        return copy(self)


    def revise_prop(self, obj_prop):
        # TODO: add a check of the form and the completion of the obj_prop dict
        # TODO: add a function to reformat the obj_prop dict
        return obj_prop

    
    def __repr__(self):
        return f"\n<\nclass 'mapv.object'\nname '{self.name}'\nshape '{self.shape}'\ncolor '{self.color}'\nmass {self.mass}kg\nacceleration {self.acceleration}m/s^2\nvelocity {self.velocity}\nposition {self.position}\n>\n"
