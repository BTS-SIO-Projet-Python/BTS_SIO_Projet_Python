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


def <variableCollision(GentilX, GentilY, EnnemieX, EnnemieY):


distance = math.sqrt(math.pow(ennemieX - gentilX) / 2) + math.pow(EnnemieY - GentilY) / 2
if distance < < distanceSouhaité >:
    return True
else:
    return False


def __init__(self):
    # creer la fenetre du jeu
    self.screen = pygame.display.set_mode((800, 600))

    # charger la carte (tmx)


tmx_data = pytmx.until_pygame.load_pygame('carte.tmx')
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyschroll.othographic.BufferedRenderer(map_data, self.screen.get_size())

# dessiner le groupe de calques
self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

K_BACKSPACE   \b
backspace
K_TAB         \t
tab
K_CLEAR
clear
K_RETURN      \r
return
K_PAUSE
pause
K_ESCAPE ^ [escape
            K_SPACE               space
            K_EXCLAIM     !       exclaim
K_QUOTEDBL
"       quotedbl
K_HASH  # hash
K_DOLLAR      $       dollar
K_AMPERSAND & ampersand
K_QUOTE
quote
K_LEFTPAREN(left
parenthesis
K_RIGHTPAREN  )       right
parenthesis
K_ASTERISK * asterisk
K_PLUS + plus
sign
K_COMMA, comma
K_MINUS - minus
sign
K_PERIOD.period
K_SLASH / forward
slash
K_0
0
0
K_1
1
1
K_2
2
2
K_3
3
3
K_4
4
4
K_5
5
5
K_6
6
6
K_7
7
7
K_8
8
8
K_9
9
9
K_COLON: colon
K_SEMICOLON;
semicolon
K_LESS < less - than
sign
K_EQUALS = equals
sign
K_GREATER > greater - than
sign
K_QUESTION    ?       question
mark
K_AT @ at
K_LEFTBRACKET[left
bracket
K_BACKSLASH   \       backslash
K_RIGHTBRACKET]      right
bracket
K_CARET ^ caret
K_UNDERSCORE
_
underscore
K_BACKQUOTE
`       grave
K_a
a
a
K_b
b
b
K_c
c
c
K_d
d
d
K_e
e
e
K_f
f
f
K_g
g
g
K_h
h
h
K_i
i
i
K_j
j
j
K_k
k
k
K_l
l
l
K_m
m
m
K_n
n
n
K_o
o
o
K_p
p
p
K_q
q
q
K_r
r
r
K_s
s
s
K_t
t
t
K_u
u
u
K_v
v
v
K_w
w
w
K_x
x
x
K_y
y
y
K_z
z
z
K_DELETE
delete
K_KP0
keypad
0
K_KP1
keypad
1
K_KP2
keypad
2
K_KP3
keypad
3
K_KP4
keypad
4
K_KP5
keypad
5
K_KP6
keypad
6
K_KP7
keypad
7
K_KP8
keypad
8
K_KP9
keypad
9
K_KP_PERIOD.keypad
period
K_KP_DIVIDE / keypad
divide
K_KP_MULTIPLY * keypad
multiply
K_KP_MINUS - keypad
minus
K_KP_PLUS + keypad
plus
K_KP_ENTER    \r
keypad
enter
K_KP_EQUALS = keypad
equals
K_UP
up
arrow
K_DOWN
down
arrow
K_RIGHT
right
arrow
K_LEFT
left
arrow
K_INSERT
insert
K_HOME
home
K_END
end
K_PAGEUP
page
up
K_PAGEDOWN
page
down
K_F1
F1
K_F2
F2
K_F3
F3
K_F4
F4
K_F5
F5
K_F6
F6
K_F7
F7
K_F8
F8
K_F9
F9
K_F10
F10
K_F11
F11
K_F12
F12
K_F13
F13
K_F14
F14
K_F15
F15
K_NUMLOCK
numlock
K_CAPSLOCK
capslock
K_SCROLLOCK
scrollock
K_RSHIFT
right
shift
K_LSHIFT
left
shift
K_RCTRL
right
control
K_LCTRL
left
control
K_RALT
right
alt
K_LALT
left
alt
K_RMETA
right
meta
K_LMETA
left
meta
K_LSUPER
left
Windows
key
K_RSUPER
right
Windows
key
K_MODE
mode
shift
K_HELP
help
K_PRINT
print
screen
K_SYSREQ
sysrq
K_BREAK
break
K_MENU
menu
K_POWER
power
K_EURO
Euro

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

        if playerX <= 0:
            playerX = 0
        elif playerX >= < -TailleDuPerso >:
            playerX = < oùOnVeut - TailleDuPerso >

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
