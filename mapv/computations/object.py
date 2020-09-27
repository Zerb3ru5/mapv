class Object(dict):

    '''
    The :class: Object is a 
    '''

    default_obj = {
        'name': 'Samuel',
        'appearance':{
            'shape': 'circle',
            'colour': 'red'
        },
        'mass': 1, # the mass in grams
        'velocity': [0, 0], # the velocity as two seperate velocity vectors, in m/s
        'acceleration': [0, 0], # the acceleration as two seperate acceleration vectors in m/s
        'position': [0, 0], # the position in kartesian coordinates
    }

    def __init__(self, obj_prop, dim=2):
        super(Object, self).__init__()

        # set the inner dict to the revised object information
        super().update(self.revise_prop(obj_prop))


    def revise_prop(self, obj_prop):
        # TODO: add a check of the form and the completion of the obj_prop dict
        # TODO: add a function to reformat the obj_prop dict
        return self.default_obj

    
    def __repr__(self):
        return f"<class 'mapv.object'><name '{super().get('name')}'>"
