"""Fachada que implementa el juego y crea los demas patrones de diseño"""
import pygame
from prototype.factory import circle_creator
from iterator.agregado import agregate
  
class FachadaJuego:

    def __init__(self):
        self.NEGRO = (0, 0, 0)
        self.BLANCO =(255,255,255)
        self.dimension_x = 1000
        self.dimension_y = 600
        self.dimensiones = (self.dimension_x, self.dimension_y)
        self.pantalla = pygame.display.set_mode(self.dimensiones)


    def Play(self):
        #Características de pantalla
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
            principal_player.movimiento_jugador(xm, ym ,self.dimension_x, self.dimension_y)
            
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
                principal_player.comer(circle)
                while True:
                    player = iterador_player.has_next()
                    if player == None:
                        break
                    player.comer(circle)
            #---Circulos_player vs. circulos_player_ppal
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                principal_player.comer(player)

            #---Circulos_player vs. circulos_player
            for a in range(len(lista_jugadores)):
                for b in range(len(lista_jugadores)):
                    if b != a:
                        lista_jugadores[a].comer(lista_jugadores[b])

            #---Código de dibujo----
            self.pantalla.fill(self.NEGRO)
            #--Todos los dibujos van después de esta línea
    
            while True:
                circle = iterador_circles.has_next()
                if circle == None:
                    break 
                circle.dibujar(self.pantalla)

            #dibujo principal player
            principal_player.dibujar(self.pantalla)

            #dibujo jugadores IA
            while True:
                player = iterador_player.has_next()
                if player == None:
                    break
                player.dibujar(self.pantalla)
           
            # Dibujo del Score
            score_y = 5
            for i in range(len(lista_jugadores)):
                self.pantalla.blit(
                    scoreText.render(str(int(lista_jugadores[i].get_radio())),
                    True, 
                    lista_jugadores[i].get_color()),(900,score_y))
                score_y = score_y + 50
            
            self.pantalla.blit(scoreText.render(str(int(principal_player.get_radio())), True, self.BLANCO),(5,5))
            #--Todos los dibujos van antes de esta línea
            pygame.display.flip()
            reloj.tick(20)  # Limitamos a 20 fotogramas por segundo

        pygame.quit()

    def inicio_juego(self):
        #Características de pantalla
        pygame.init()
        pygame.display.set_caption("Inicio")

        #CONFIGURACION DE SCORE FUENTE    
        scoreText=pygame.font.Font(None, 100)
        scoreText2=pygame.font.Font(None, 20)

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
            pygame.event.pump()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                terminar = True

            #---Código de dibujo----
            self.pantalla.fill(self.NEGRO)

            #--Todos los dibujos van después de esta línea
            
            self.pantalla.blit(scoreText
                .render("Agar.io", True, self.BLANCO),((self.dimension_x/2)-120,(self.dimension_y/2)-100))
            self.pantalla.blit(scoreText2
                .render("Presione ESPACIO para comenzar", True, self.BLANCO),((self.dimension_x/2)-120,(self.dimension_y/2)+50))
            #--Todos los dibujos van antes de esta línea
            pygame.display.flip()
            reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
