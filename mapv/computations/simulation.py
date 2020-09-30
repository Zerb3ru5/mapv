'''
A simulation is the connection of a model with the objects, the model defines the rules for.
'''


from mapv.computations.object import Object
from mapv.computations.model import Model
from mapv.computations.state import State

import numpy as np


class Simulation():

    boundaries = []
    model = int()
    initial_state = State(time=0)
    current_state = State(time=0)
    states = []

    def __init__(self):

        # load information about this particular simulation
        

        # create the objects in the simulation based on the information from the file
        obj = Object(
            dim=2,
            obj_prop={}
        )
        self.initial_state.objects.append(obj)

        self.current_state = self.initial_state

        # set the model this simulation uses
        self.model = Model(
            model_prop={}
        )

        # define the boundaries
        self.boundaries = ['time', 0, 40]


    def simulate(self):
        '''
        Calculate all the different states on by another until the boundaries are fulfilled.
        '''

        time = 0

        # add the inital state
        self.states.append(self.initial_state)
        
        while self.in_boundaries(self.states[-1]):
            time += 1
            self.states.append(self.iterate(time=time))
            print('tadaaa')

        print('States: ', self.states)


    def in_boundaries(self, last_state):

        if last_state.time < 40:
            return True
        else:
            return False


    def iterate(self, time):
        '''
        Calculates the next iteration of the simulation

        Projectile motion

        time = 0
        initial pos = s_0
        position = [s_x, s_y]
        inital vel = v_0
        velocity = [v_x, v_y]
        acceleration = [a_x, a_y = g]
        '''

        object = self.states[-1].objects[0]

        t = float(time)

        s_0 = float(0)
        s = np.array([object['position'][0], object['position'][1]])
        v_0 = float(0)
        v = np.array([object['velocity'][0], object['velocity'][1]])

        a = np.array([object['acceleration'][0], object['acceleration'][1]])

        print('time ', t, ', init pos ', s_0, ', position ', s, ', init velocity ', v_0, ', velocity ', v, ', acceleration ', a )

        # temporary
        s[0] = v[0] * t
        s[1] = s_0 + v_0 * t + 1 / 2 * a[1] * (t) ** 2

        v[0] = a[0] * t
        v[1] = a[1] * t

        # copy the latest state and fill in the new values
        new_state = self.current_state.copy()
        print(new_state)

        new_state.time = time
        new_state.objects[0]['position'] = s
        new_state.objects[0]['velocity'] = v

        self.current_state = new_state

        return new_state
