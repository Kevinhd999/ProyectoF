import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False
        self.animaciones = animaciones
        #Imagen de la animacion que se esta mostrando actualmente
        self.frame_index = 0 
        #Aqui se almacena la hora actual (en milisegundo desde que se inicio 'pygame')
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)

    def Movimiento (self, delta_x, delta_y):

        #Define el lado de el movimiento del personaje
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False 

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

    #Llamar
    def update(self):
        cooldown_animacion = 500
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0


    def dibujar (self, interfaz):
        #Me va aguardar la transformacion de la varible
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_BLANCO, self.forma,1.1)

    