import random
from .prototypes import circulo_food, circulo_player, circulo_principal_player

class circle_creator():
    def __init__(self):
        self.__circulo__ = circulo_food()
        self.__player__ = circulo_player()
        self.__principal_player__ = circulo_principal_player()

    def get_circle(self, kind_of_circle):
        if "food" == kind_of_circle:
            self.__circulo__.set_position(random.randrange(1000), random.randrange(600))
            self.__circulo__.set_color(random.randrange(255), random.randrange(255), random.randrange(255))
            return self.__circulo__.clone()          
        elif "player" == kind_of_circle:
            self.__player__.set_position(random.randrange(1000), random.randrange(600))
            self.__player__.set_color(random.randrange(255), random.randrange(255), random.randrange(255))
            return self.__player__.clone()
        elif "principal_player" == kind_of_circle:
            self.__principal_player__.set_position(random.randrange(1000), random.randrange(600))
            self.__principal_player__.set_color(random.randrange(255), random.randrange(255), random.randrange(255))
            return self.__principal_player__.clone()


    