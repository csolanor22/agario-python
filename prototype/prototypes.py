import random
import pygame
from copy import deepcopy

class circulo(object):
    def __init__(self, posicion, color, radio):
        self.position = posicion
        self.color = color
        self.radio = radio

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

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla,self.color,self.position, int(self.radio))

class circulo_food(circulo):
    def __init__(self):
        position = [random.randrange(800), random.randrange(600)]
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
        radio = 2
        circulo.__init__(self, position, color, radio)
    

class circulo_player(circulo):
    def __init__(self):
        position = [random.randrange(800), random.randrange(600)]
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
        radio = 8

        circulo.__init__(self, position, color, radio)

        self.limite_x = 1
        self.limite_y = 1
        self.velocidad = 3

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

    def movimiento_jugadores(self):
        x, y = self.position
        if x >= 1000 or self.limite_x == 1:
            self.velocidad = 1
            x = x - self.velocidad
            if x <= 0:
                self.limite_x = 0
        else:
            x = x + self.velocidad
        if y >= 600 or self.limite_y == 1:
            self.limite_y = 1
            y = y - self.velocidad
            if y <= 0:
                self.limite_y = 0
        else:
            y = y + self.velocidad
        self.position = (x, y)
    
class circulo_principal_player(circulo):
    def __init__(self):
        position = [random.randrange(800), random.randrange(600)]
        color = (random.randrange(255), random.randrange(255), random.randrange(255))
        radio = 8

        circulo.__init__(self, position, color, radio)

        self.velocidad = 3

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def movimiento_jugador(self, x, y, dimension_x, dimension_y):
        xp, yp = self.position
        if x < xp and x < dimension_x:
            xp = xp - self.velocidad
        else:
            xp = xp + self.velocidad
        if y < yp and y < dimension_y:
            yp = yp - self.velocidad
        else:
            yp = yp + self.velocidad
        self.position = (xp, yp)