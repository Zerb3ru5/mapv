import pyglet

class Visualization():
    def __init__(self):
        self.window = pyglet.window.Window()

        label = pyglet.text.Label('Hello World',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x = window.width // 2,
                                  y = window.height // 2,
                                  anchor_x = 'center',
                                  anchor_y = 'center')

        

        pyglet.app.run()