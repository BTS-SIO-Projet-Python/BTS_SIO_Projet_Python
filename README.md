Documents où le code est mit. 
src : https://ztiromoritz.github.io/pico-8-shooter/
src : http://www.pixelart.name/pixel-art-8x8/

import pygame

pygame.init ()

screen = pygame.display.set_mode((800, 800))

#Icone du jeu
pygame.display.set_caption('Dead By Deadline')
<NomDeVariablePourImage> = pygame.image.load('<oùElleEst>')
pygame.display.set_icon(<NomDeVariablePourImage>)

 # Instancier le player
playerImg = pygame.image.load('Deadpull.png')
playerX = 200
playerY = 200
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True 

while running :

    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.k_RIGHT:
                playerX_change = 0



    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
  
  
  
  #Pour rajouter des bords :   
  if playerX <= 0:
        playerX =0
    elif playerX >= <oùOnVeut-TailleDuPerso>:
        playerX = <oùOnVeut-TailleDuPerso>
  
  #Collision
  
  def <variableCollision( GentilX,GentilY , EnnemieX, EnnemieY):
         distance = math.sqrt(math.pow(ennemieX - gentilX) / 2) + math.pow(EnnemieY - GentilY) / 2
