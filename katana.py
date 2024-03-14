import pygame
import constantes
import math

class Katana():
    def __init__(self, image, imagen_fuego):
        self.imagen_fuego = imagen_fuego
        self.imagen_original = image
        self.angulo = 0
        self.imagen = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.forma = self.imagen.get_rect()


    def update(self, personaje):
        fuego = None
        self.forma.center = personaje.forma.center
        if personaje.flip == False:
            self.forma.x = self.forma.x + personaje.forma.width/4
            self.forma.y = self.forma.y - 35
            self.rotar_arma (True)
        if personaje.flip == True:
            self.forma.x = self.forma.x - personaje.forma.width/4
            self.forma.y = self.forma.y - 35
            self.rotar_arma (False)


        #Mover la pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x =mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y,distancia_x))

        #detectar los clicks de mouse 
        if pygame.mouse.get_pressed()[0]:
            fuego = Elemento(self.imagen_fuego, self.forma.centerx, self.forma.centery, self.angulo) 
        return fuego
    

    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                True, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)
        else:
            imagen_flip = pygame.transform.flip(self.imagen_original,
                                                False, False)
            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen,
                                              self.angulo)
        interfaz.blit(self.imagen, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_BLANCO, self.forma, 1)


class Elemento(pygame.sprite.Sprite):
    def __init__(self, image,x,y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.image_original, self.angulo) 
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def dibujar (self,interfaz):
        interfaz.blit(self.image, (self.rect.centerx,
                                    self.rect.centery ))   






