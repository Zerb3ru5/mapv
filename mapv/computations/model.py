from mapv.computations.point import Point


class Model():
    '''
    A `Model` describes the rules, the conditions, when these rules are applied on, 
    and some environmental variables of the simulation. It calculates the different 
    timesteps for the objects (and therewith the simulation)

    ...

    Attributes
    ----------
    name : str
        the name of the model
    dimension : int, optional
        the dimensions the rules are applied in (Is our virtual world in 2D or 3D?), defaults to 1

    Methods
    -------
    iter(object, time):
        calculates the timestep for the time given
    '''

    def __init__(self, name, dimension=1):
        
        self.name = name

    
    def iter(self, object, time):
        '''
        Calculates the timestep for the given time

        Parameters
        ----------
        object : Object
            the object the timestep is calculated for
        time : float
            the time the timestep is set on

        Returns
        -------
        velocity : float
            the new velocity of the object
        position : Point
            the new position of the object
        '''

        velocity = object.velocity[0] + object.acceleration * time
        position = object.position[0].x + object.velocity[0] * time + (object.acceleration * (time ** 2)) / 2

        return velocity, Point(x=position, dimension=1)