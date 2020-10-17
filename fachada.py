"""Fachada que implementa el juego y crea los demas patrones de diseño"""
import random
import pygame
from prototype.factory import circle_creator
from iterator.agregado import agregate
  
class FachadaJuego:

    def movimiento_jugadores(self, player):
        x, y = player.get_position()
        limitex = player.get_limite_x()
        limitey = player.get_limite_y()
        velocidad = player.get_velocidad()
        if x >= 1000 or limitex == 1:
            player.set_limite_x(1)
            x = x - velocidad
            if x <= 0:
                player.set_limite_x(0)
        else:
            x = x + velocidad
            
        if y >= 600 or limitey == 1:
            player.set_limite_y(1)
            y = y - velocidad
            if y <= 0:
                player.set_limite_y(0)
        else:
            y = y + velocidad  
        player.set_position(x, y)

    def comparacion_circulos(self, circulo_p, circulo_f):
        x = abs(circulo_p.get_position()[0] - circulo_f.get_position()[0])
        y = abs(circulo_p.get_position()[1] - circulo_f.get_position()[1])
        circulo_p_radio = circulo_p.get_radio()
        circulo_f_radio = circulo_f.get_radio()
        if  x <= circulo_p_radio and y <= circulo_p_radio:
            circulo_f.set_position(random.randrange(1000),random.randrange(600))
            if circulo_f_radio <= 3:
                circulo_p.set_radio(circulo_p_radio + 0.1)
            else:
                circulo_p.set_radio(circulo_p_radio + (circulo_f_radio*0.1))
                circulo_f.set_radio(8)
        if  x <= circulo_f_radio and y <= circulo_f_radio:
            circulo_p.set_position(random.randrange(1000),random.randrange(600))
            circulo_f.set_radio((circulo_p_radio*0.1) + circulo_f_radio)
            circulo_p.set_radio(8)
            circulo_p.set_velocidad(3)
        if circulo_p_radio > 15:
            circulo_p.set_velocidad(2)
        if circulo_p_radio > 25:
            circulo_p.set_velocidad(1)
        if circulo_p_radio < 15:
            circulo_p.set_velocidad(3)

    def Play(self):
        #Colores
        NEGRO = (0, 0, 0)
        BLANCO =(255,255,255)

        cantidad_circulos = 2000

        #Características de pantalla
        pygame.init()
        dimension_x = 1000
        dimension_y = 600
        dimensiones = (dimension_x, dimension_y)
        Pantalla = pygame.display.set_mode(dimensiones)
        pygame.display.set_caption("Agar.io")

        lista_circulos = []
        #--- Prototype circulos creator
        creator = circle_creator()

        #--- Iterador agregate
        agregado = agregate()

        for i in range(cantidad_circulos):
            lista_circulos.append(creator.get_circle("food"))

        #enemy
        lista_jugadores = []
        cantidad_jugadores = 5
        for i in range(cantidad_jugadores):
            lista_jugadores.append(creator.get_circle("player"))

        #--- Creamos iterador para los jugadores y los circulos
        iterador_player = agregado.get_iterador(lista_jugadores)
        iterador_circles = agregado.get_iterador(lista_circulos)

        #jugador
        principal_player = creator.get_circle("player")

        Terminar = False
        #Se define para poder gestionar cada cuando se ejecuta un fotograma
        reloj = pygame.time.Clock()

        while not Terminar:
            #---Manejo de eventos
            for Evento in pygame.event.get():
                if Evento.type == pygame.QUIT:
                    Terminar = True

        #---La lógica del juego

            #---Movimiento del circulo
            x, y = pygame.mouse.get_pos()
            xp, yp = principal_player.get_position()

            if x < xp and x < dimension_x:
                xp = xp - principal_player.get_velocidad()
            else:
                xp = xp + principal_player.get_velocidad()
            if y < yp and y < dimension_y:
                yp = yp - principal_player.get_velocidad()
            else:
                yp = yp + principal_player.get_velocidad()
            principal_player.set_position(xp, yp)
            
            #---Movimiento enemy
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                FachadaJuego.movimiento_jugadores(self, player)

            #-Comparacion de circulos
            #---Circulos_food vs. circulos_player 
            while True:
                circle = iterador_circles.has_next()
                if circle == None:
                    break
                FachadaJuego.comparacion_circulos(self, principal_player, circle)
                while True:
                    player = iterador_player.has_next()
                    if player == None:
                        break
                    FachadaJuego.comparacion_circulos(self, player, circle)
            #---Circulos_player vs. circulos_player_ppal
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                FachadaJuego.comparacion_circulos(self, principal_player, player)      

            #CONFIGURACION DE SCORE FUENTE    
            scoreText=pygame.font.Font(None, 40)
            iterador_circles = agregado.get_iterador(lista_circulos)

            #---Código de dibujo----
            Pantalla.fill(NEGRO)
            #--Todos los dibujos van después de esta línea
    
            while True:
                circle = iterador_circles.has_next()
                if circle == None:
                    break 
                pygame.draw.circle(Pantalla, circle.get_color(), circle.get_position(), int(circle.get_radio()))
           
            # Dibujo del Score
            score_y = 5
            for i in range(len(lista_jugadores)):
                Pantalla.blit(
                    scoreText.render(str(int(lista_jugadores[i].get_radio())),
                    True, 
                    lista_jugadores[i].get_color()),(900,score_y))
                score_y = score_y + 50
            
            #DIBUJO PLAYER
            pygame.draw.circle(Pantalla, principal_player.get_color(), principal_player.get_position(), int(principal_player.get_radio()))

            #DIBUJO IA
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                pygame.draw.circle(Pantalla,player.get_color(),player.get_position(), int(player.get_radio()))
            
            Pantalla.blit(scoreText.render(str(int(principal_player.get_radio())), True, BLANCO),(5,5))
            #--Todos los dibujos van antes de esta línea
            pygame.display.flip()
            reloj.tick(20)  # Limitamos a 20 fotogramas por segundo

        pygame.quit()