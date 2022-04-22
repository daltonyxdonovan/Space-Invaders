import pygame, sys, time
from bullets import Bullet
from playerShip import Ship
from enemyShip import alienShip
from bgmove import BGMove
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
#CONSTANTS
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
SCREEN_HEIGHT, SCREEN_WIDTH = 800,800
pygame.display.set_caption("space invaders bullshit")
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
myfont = pygame.font.SysFont("monospace", 40, bold=True)
#VARIABLES
clock = pygame.time.Clock()
vel = 3
avel = 2
playerx = 200
playery = 600
score = 0
game_on = True
bulletsok = False
right = True
left = False
down = False
justStarting = True
#ship thingy
backgroundmovement = pygame.sprite.Group()
bgmove = BGMove(GREEN, 100, 350, -10)
bgmove.rect.x = 0
bgmove.rect.y = 0
backgroundmovement.add(bgmove)
mainSpriteGroup = pygame.sprite.Group()
playerShip = Ship(BLACK, 8, 50, 50)
playerShip.rect.x = playerx
playerShip.rect.y = playery
mainSpriteGroup.add(playerShip)
Bullets = pygame.sprite.Group()
bulletload = Bullet(RED, 10,10,2)
bulletload.rect.x = (playerShip.rect.x + 20)
bulletload.rect.y = (playerShip.rect.y - 20)
Bullets.add(bulletload)
#aliens
Aliens = pygame.sprite.Group()
alien = alienShip(GREEN, 8, 50, 50)
alien.rect.x = 140
alien.rect.y = 40
Aliens.add(alien)
alien2 = alienShip(GREEN, 8, 50, 50)
alien2.rect.x = 40
alien2.rect.y = 40
Aliens.add(alien2)
alien3 = alienShip(GREEN, 8, 50, 50)
alien3.rect.x = 340
alien3.rect.y = 40
Aliens.add(alien3)
alien4 = alienShip(GREEN, 8, 50, 50)
alien4.rect.x = 240
alien4.rect.y = 40
Aliens.add(alien4)
alien5 = alienShip(GREEN, 8, 50, 50)
alien5.rect.x = 140
alien5.rect.y = -10
Aliens.add(alien5)
alien6 = alienShip(GREEN, 8, 50, 50)
alien6.rect.x = 40
alien6.rect.y = -10
Aliens.add(alien6)
alien7 = alienShip(GREEN, 8, 50, 50)
alien7.rect.x = 340
alien7.rect.y = -10
Aliens.add(alien7)
alien8 = alienShip(GREEN, 8, 50, 50)
alien8.rect.x = 240
alien8.rect.y = -10
Aliens.add(alien8)
alien9 = alienShip(GREEN, 8, 50, 50)
alien9.rect.x = 140
alien9.rect.y = -60
Aliens.add(alien9)
alien10 = alienShip(GREEN, 8, 50, 50)
alien10.rect.x = 40
alien10.rect.y = -60
Aliens.add(alien10)
alien11 = alienShip(GREEN, 8, 50, 50)
alien11.rect.x = 340
alien11.rect.y = -60
Aliens.add(alien11)
alien12 = alienShip(GREEN, 8, 50, 50)
alien12.rect.x = 240
alien12.rect.y = -60
Aliens.add(alien12)
alien13 = alienShip(GREEN, 8, 50, 50)
alien13.rect.x = 140
alien13.rect.y = -110
Aliens.add(alien13)
alien14 = alienShip(GREEN, 8, 50, 50)
alien14.rect.x = 40
alien14.rect.y = -110
Aliens.add(alien14)
alien15 = alienShip(GREEN, 8, 50, 50)
alien15.rect.x = 340
alien15.rect.y = -110
Aliens.add(alien15)
alien16 = alienShip(GREEN, 8, 50, 50)
alien16.rect.x = 240
alien16.rect.y = -110
Aliens.add(alien16)
#images for the aliens and player
def WorldImg(x, y):
	worldimg = pygame.image.load('world.png').convert_alpha()
	screen.blit(worldimg, (x, y))
def background(x, y):
	bgimg = pygame.image.load('background2.png').convert_alpha()
	screen.blit(bgimg, (x, y))
#stuff
while game_on:
	background(bgmove.rect.x,0)
	Aliens.update()
	Aliens.draw(screen)
	mainSpriteGroup.draw(screen)
	sprite_collision_list = pygame.sprite.groupcollide(Bullets,Aliens,False, True)
	for sprite in sprite_collision_list:
		bulletsok = False
		score += 100
		print("\nThe alien's velocity is: " + str(avel) + " pixels.")
		print("Your score is: " + str(score))
	#rules for movement
	if right == True:
		alien.rect.x += avel
		alien2.rect.x += avel
		alien3.rect.x += avel
		alien4.rect.x += avel
		alien6.rect.x += avel
		alien7.rect.x += avel
		alien8.rect.x += avel
		alien5.rect.x += avel
		alien9.rect.x += avel
		alien10.rect.x += avel
		alien11.rect.x += avel
		alien12.rect.x += avel
		alien13.rect.x += avel
		alien14.rect.x += avel
		alien15.rect.x += avel
		alien16.rect.x += avel
	if left == True:
		alien.rect.x -= avel
		alien2.rect.x -= avel
		alien3.rect.x -= avel
		alien4.rect.x -= avel
		alien6.rect.x -= avel
		alien7.rect.x -= avel
		alien8.rect.x -= avel
		alien5.rect.x -= avel
		alien9.rect.x -= avel
		alien10.rect.x -= avel
		alien11.rect.x -= avel
		alien12.rect.x -= avel
		alien13.rect.x -= avel
		alien14.rect.x -= avel
		alien15.rect.x -= avel
		alien16.rect.x -= avel
	if down == True:
		alien.rect.y += avel
		alien2.rect.y += avel
		alien3.rect.y += avel
		alien4.rect.y += avel
		alien6.rect.y += avel
		alien7.rect.y += avel
		alien8.rect.y += avel
		alien5.rect.y += avel
		alien9.rect.y += avel
		alien10.rect.y += avel
		alien11.rect.y += avel
		alien12.rect.y += avel
		alien13.rect.y += avel
		alien14.rect.y += avel
		alien15.rect.y += avel
		alien16.rect.y += avel
	#y axis logic
	if alien4.rect.y >= 100:
		down = False
		right = False
		avel = 2
		left = True
	if alien4.rect.y >= 150:
		left = False
		down = False
		avel = 3
		right = True
	if alien4.rect.y >= 250:
		down = False
		right = False
		avel = 4
		left = True
	if alien.rect.y >= 350:
		down = False
		left = False
		avel = 5
		right = True
	if alien4.rect.y >= 450:
		down = False
		right = False
		avel = 6
		left = True
	if alien4.rect.y >= 550:
		left = False
		down = False
		avel = 7
		right = True
	if alien4.rect.y >= 650:
		quit()
	#x axis logic
	if alien.rect.x < 140:
		left = False
		down = True
	if alien4.rect.x >= 600:
		right = False
		down = True
	#keypress stuff
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bulletsok = True
			if event.key == pygame.K_UP:
				avel = avel + 1
	#draw bullets
	if bulletsok == True:
		bulletload.rect.y -= vel*8
		Bullets.draw(screen)
	#bullet reset logic
	if bulletsok == False:
		bulletload.rect.x = (playerShip.rect.x + 20)
		bulletload.rect.y = (playerShip.rect.y - 20)
	if bulletload.rect.y <= 1:
		bulletsok = False
		bulletload.rect.x = (playerShip.rect.x + 20)
		bulletload.rect.y = (playerShip.rect.y - 20)
	if keys[pygame.K_ESCAPE]:
		quit()
	if keys[pygame.K_LEFT]:
		playerShip.rect.x -= (vel*4)
	if keys[pygame.K_RIGHT]:
		playerShip.rect.x += (vel*4)
	#ship boundaries
	if playerShip.rect.x <= -50:
		playerShip.rect.x = 799
	if playerShip.rect.x >= 800:
		playerShip.rect.x = -49
	WorldImg(0,700)
	pygame.display.update()
	pygame.display.flip()
	clock.tick(30)
