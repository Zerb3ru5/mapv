'''
A simulation is the connection of a model with the objects, the model defines the rules for.
'''


from mapv.computations.object import Object
from mapv.computations.model import Model
from mapv.computations.point import Point
from mapv.computations.util.vector import Vector

import numpy as np
import math
import mapv.visuals.visualization

import click


class Simulation():

    def __init__(self, name):

        # load the objects into the simulation
        self.objects = []

        for i in range(1):
            self.objects.append(Object(
                obj_prop={
                    'name': 'Hubert',
                    'shape': 'circle',
                    'color': 'red',
                    'mass': 10.0,
                    'acceleration': 2.0,
                    'velocity': 0.0,
                    'position': Point(0.0)
                },
                dimension=1))

        print(self.objects)

        # load the model into the simulation
        self.model = Model('Arnold')

    def simulate(self):

        time = 1
        boundary = 10

        # iterate through all the timesteps and add them to the objects
        while time < boundary + 1:
            for object in self.objects:
                velocity, position = self.model.iter(object, time)
                object.add_timestep(velocity, position)
            time += 1

        print(self.objects)

