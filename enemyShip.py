import pygame
WHITE = (255, 255, 255)
GREEN = (0,255,0)
BLUE = (100, 100, 255)
count = 0

SCREEN_HEIGHT, SCREEN_WIDTH = 800,800
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

def load_image(name):
    image = pygame.image.load(name)
    return image
class alienShip(pygame.sprite.Sprite):
	def __init__(self, color, speed, height, width):
		super().__init__()
		self.color = color
		self.speed = speed
		self.height = height
		self.width = width
		self.images = []
		self.images.append(load_image('bugship.png'))
		self.images.append(load_image('bugship2.png'))
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 48, 48)
	def update(self):
		global count
		count += 1
		if count >= 20:
			self.index += 1
			count = 0
		if self.index > 1:
			self.index = 0
		self.image = self.images[self.index]
	def moveLeft(self, pixels):
		self.rect.x -= pixels
	def moveRight(self, pixels):
		self.rect.x += pixels
def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = TestSprite()
	my_group = pygame.sprite.Group(my_sprite)
	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		my_group.update()
		my_group.draw(screen)
		pygame.display.flip()
	if __name__ == '__main__':
		main()
