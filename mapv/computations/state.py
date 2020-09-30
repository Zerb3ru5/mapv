from copy import copy


class State():
    '''
    A :class: State stores the values of all the objects in a simulation at a given time.
    '''

    def __init__(self, time):

        self.time = time
        self.objects = []


    def copy(self):
        return copy(self)


    def __repr__(self):
        return f"<class 'mapv.simulation.state'><time {self.time}, object {self.objects}>"