import random
from copy import deepcopy

class circulo_food():
    def __init__(self):
        self.position = [random.randrange(800), random.randrange(600)]
        self.color = (random.randrange(255), random.randrange(255), random.randrange(255))
        self.radio = 2

    def set_position(self, x, y):
        self.position = [x,y]
    
    def get_position(self):
        return self.position

    def set_color(self, r, g, b):
        self.color = (r,g,b)

    def get_color(self):
        return self.color

    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio
    
    def clone(self):
        return deepcopy(self)

class circulo_player():
    def __init__(self):
        self.position = [random.randrange(800), random.randrange(600)]
        self.color = (random.randrange(255), random.randrange(255), random.randrange(255))
        self.radio = 8
        self.limite_x = 1
        self.limite_y = 1
        self.velocidad = 3

    def set_position(self, x, y):
        self.position = (x,y)

    def get_position(self):
        return self.position

    def set_color(self, r, g, b):
        self.color = (r,g,b)

    def get_color(self):
        return self.color
        
    def get_radio(self):
        return self.radio

    def set_radio(self, radio):
        self.radio = radio

    def get_limite_x(self):
        return self.limite_x

    def set_limite_x(self, limite_x):
        self.limite_x = limite_x

    def get_limite_y(self):
        return self.limite_y

    def set_limite_y(self, limite_y):
        self.limite_y = limite_y
    
    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    
    def clone(self):
        return deepcopy(self)
