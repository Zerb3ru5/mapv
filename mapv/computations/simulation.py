'''
A simulation is the connection of a model with the objects, the model defines the rules for.
'''


from mapv.computations.object import Object


class Simulation():
    def __init__(self):

        # load information about this particular simulation
        
        # create the objects in the simulation based on the information from the file
        objects = []
        obj = Object(
            dim=2,
            obj_prop={}
        )

        print(obj)