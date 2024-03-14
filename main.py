import pygame 
import sys 
import constantes
from personaje import Personaje
from katana import Katana

pygame.init()

#Ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

#Controlar los fps
clock = pygame.time.Clock()

#Nombre de la ventana
pygame.display.set_caption("Juego Final")


#Tamano Personaje y Arma funcion
def escalar_img (image,  scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen


#Importar Imagenes
#Personaje
animaciones = []
for i in range (8):
    img = pygame.image.load(f"assets//images//player/run/run_{i}.png").convert_alpha()
    img = escalar_img (img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)

#Arma
#Convert alpha mejora la calidad
    imagen_espada = pygame.image.load("./assets/images/katana/katana.png").convert_alpha()
    imagen_espada = escalar_img (imagen_espada, constantes.ESCALA_KATANA)


#Fuego
#Convert alpha mejora la calidad
    imagen_fuegos = pygame.image.load("./assets/images/katana/fuego.png").convert_alpha()
    imagen_fuegos = escalar_img (imagen_fuegos, constantes.ESCALA_FUEGO)


#Crear un jugador de la clase personaje
jugador = Personaje(50,50, animaciones)

#Crear una clase katana
espada = Katana(imagen_espada, imagen_fuegos)

#Crear un grupo de sprite

grupo_fuegos = pygame.sprite.Group()


#Definir las variables de movimientos del jugador
mover_arriba = False
mover_izquierda = False
mover_abajo = False
mover_derecha = False

juego = True

while juego :

    #Indicar los FPS
    clock.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)


    #Calcular el movimiento de el jugador
    delta_x = 0 
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = constantes.VELOCIDADN
    if mover_arriba == True:
        delta_y = constantes.VELOCIDADN
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #Mover al jugador
    jugador.Movimiento(delta_x,delta_y)
    #Actualiza el estado del jugador 
    jugador.update()
    #Actualiza el estado del arma 
    fuego = espada.update(jugador)
    if fuego :
        grupo_fuegos.add(fuego)

    #Dibujar al jugador 
    jugador.dibujar(ventana)

    #Dibujar el arma
    espada.dibujar(ventana)

    #Dibujar fuego
    for fuego in grupo_fuegos:
        fuego.dibujar(ventana)



    for event in pygame.event.get():
        #Cerrar el juego
        if event.type == pygame.QUIT:
            juego = False

        #Teclas
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

            #Para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    #Actualizar el juego
    pygame.display.update()

pygame.quit()