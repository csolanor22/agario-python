"""Fachada que implementa el juego y crea los demas patrones de diseño"""
import random
import pygame
from prototype.factory import circle_creator
from iterator.agregado import agregate
  
class FachadaJuego:

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

        #Características de pantalla
        pygame.init()
        dimension_x = 1000
        dimension_y = 600
        dimensiones = (dimension_x, dimension_y)
        pantalla = pygame.display.set_mode(dimensiones)
        pygame.display.set_caption("Agar.io")

        #--- Prototype circulos creator
        creator = circle_creator()

        #--- Iterador agregate
        agregado = agregate()

        #Creación de listas de jugadores y comida
        cantidad_circulos_comida = 3000
        lista_circulos = []
        lista_jugadores = []
        cantidad_jugadores = 5

        for i in range(cantidad_jugadores):
            lista_jugadores.append(creator.get_circle("player"))

        for i in range(cantidad_circulos_comida):
            lista_circulos.append(creator.get_circle("food"))

        #--- Creamos iterador para los jugadores y los circulos
        iterador_player = agregado.get_iterador(lista_jugadores)
        iterador_circles = agregado.get_iterador(lista_circulos)

        #jugador principal
        principal_player = creator.get_circle("principal_player")

        #CONFIGURACION DE SCORE FUENTE    
        scoreText=pygame.font.Font(None, 40)

        terminar = False
        #Se define para poder gestionar cada cuando se ejecuta un fotograma
        reloj = pygame.time.Clock()

        while not terminar:
            #---Manejo de eventos
            for Evento in pygame.event.get():
                if Evento.type == pygame.QUIT:
                    terminar = True

        #---La lógica del juego

            #---Movimiento del circulo principal_player
            xm, ym = pygame.mouse.get_pos()
            principal_player.movimiento_jugador(xm, ym ,dimension_x, dimension_y)
            
            #---Movimiento enemy
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                player.movimiento_jugadores()

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

            #---Circulos_player vs. circulos_player
            for a in range(len(lista_jugadores)):
                for b in range(len(lista_jugadores)):
                    if b != a:
                        FachadaJuego.comparacion_circulos(self, lista_jugadores[a], lista_jugadores[b])

            #---Código de dibujo----
            pantalla.fill(NEGRO)
            #--Todos los dibujos van después de esta línea
    
            while True:
                circle = iterador_circles.has_next()
                if circle == None:
                    break 
                circle.dibujar(pantalla)

            #dibujo principal player
            principal_player.dibujar(pantalla)

            #dibujo jugadores IA
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                player.dibujar(pantalla)
           
            # Dibujo del Score
            score_y = 5
            for i in range(len(lista_jugadores)):
                pantalla.blit(
                    scoreText.render(str(int(lista_jugadores[i].get_radio())),
                    True, 
                    lista_jugadores[i].get_color()),(900,score_y))
                score_y = score_y + 50
            
            pantalla.blit(scoreText.render(str(int(principal_player.get_radio())), True, BLANCO),(5,5))
            #--Todos los dibujos van antes de esta línea
            pygame.display.flip()
            reloj.tick(20)  # Limitamos a 20 fotogramas por segundo

        pygame.quit()