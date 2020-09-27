'''
A simulation is the connection of a model with the objects, the model defines the rules for.
'''


from mapv.computations.object import Object
from mapv.computations.model import Model
from mapv.computations.state import State


class Simulation():

    boundaries = []
    objects = []
    model = int()

    def __init__(self):

        # load information about this particular simulation
        
        # create the objects in the simulation based on the information from the file
        obj = Object(
            dim=2,
            obj_prop={}
        )
        self.objects.append(obj)

        # set the model this simulation uses
        self.model = Model(
            model_prop={}
        )

        # define the boundaries
        self.boundaries = ['time', 0, 40]

        print(obj)


    def simulate(self):
        '''
        Calculate all the different states on by another until the boundaries are fulfilled.
        '''

        states = []
        time = 0

        # add the inital state
        states.append(State(time, self))
        
        while self.in_boundaries(states[-1]):
            time += 1
            states.append(self.iterate(time=time))
            print('tadaaa')

        print(states)


    def in_boundaries(self, last_state):
        print(last_state, last_state.time, self.boundaries[2])

        if last_state.time < self.boundaries[2]:
            print('yeah')
            return True
        else:
            print('nooo')
            return False


    def iterate(self, time):
        '''
        Calculates the next iteration of the simulation
        '''
        return State(time, self)
