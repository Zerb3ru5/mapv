class State():
    '''
    A :class: State stores the values of all the objects in a simulation at a given time.
    '''

    def __init__(self, time, simulation):

        self.time = time
        self.objects = simulation.objects


    def __repr__(self):
        return f"<class 'mapv.simulation.state'><time {self.time}>"

        