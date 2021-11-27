import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

# Icone du jeu
pygame.display.set_caption('Dead By Deadline')
< NomDeVariablePourImage > = pygame.image.load('<oùElleEst>')
pygame.display.set_icon( < NomDeVariablePourImage >)

# Instancier le player
playerImg = pygame.image.load('Deadpull.png')
playerX = 200
playerY = 200
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True

while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # POUR DEPLACER LE PERSO SELON LES FLECHES 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.k_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()

    # Pour rajouter des bords :
if playerX <= 0:
    playerX = 0
elif playerX >= < oùOnVeut - TailleDuPerso >:
    playerX = < oùOnVeut - TailleDuPerso >

    # Collision
(def <variableCollision(GentilX, GentilY, EnnemieX, EnnemieY):

distance = math.sqrt(math.pow(ennemieX - gentilX) / 2) + math.pow(EnnemieY - GentilY) / 2
if distance < < distanceSouhaité >:
    return True
else:
    return False
)

def __init__(self):
    # creer la fenetre du jeu
    self.screen = pygame.display.set_mode((800, 600))

    # charger la carte (tmx)


tmx_data = pytmx.until_pygame.load_pygame('carte.tmx')
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyschroll.othographic.BufferedRenderer(map_data, self.screen.get_size())

# dessiner le groupe de calques
self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

# Instancier le player
playerImg = pygame.image.load('chèvre.jpg')
playerX = 200
playerY = 200
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True

while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
#Collision contre les murs
        #if playerX <= 0:
         #   playerX = 0
        #elif playerX >= < -TailleDuPerso >:
         #   playerX = < oùOnVeut - TailleDuPerso >
#Ajoute valeur x et y 
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
