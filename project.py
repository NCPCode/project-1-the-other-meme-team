import pygame

class Paddles:
	def __init__(self, color, coords, size, speed):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.size = size
		self.speed = speed

	def move(self, direction):
		if direction == 'up':
			self.coords[1] -= self.speed
		elif direction == 'down':
			self.coords[1] += self.speed
	
	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.coords, self.size))

	def check_boundaries(self, screen_size):
		for i in [0, 1]:
			if (self.coords[i] < 0):
				self.coords[i] = 0
			elif (self.coords[i] >= screen_size[i] - self.size[i]):
				self.coords[i] = screen_size[i] - self.size[i]

	def reset(self):
		self.coords = list(self.initial_coords)


class Ball:
	def __init__(self, color, coords, size, speed):
		self.color = color
		self.initial_coords = list(coords)
		self.coords = coords
		self.size = size
		self.speed = speed

	def move(self, direction):
		if direction == 'up':
			self.coords[1] -= self.speed
		elif direction == 'down':
			self.coords[1] += self.speed
		elif direction == 'left':
			self.coords[0] -= self.speed
		else:
			self.coords[0] += self.speed

	def draw(self, window):
		pygame.draw.circle(window, self.color, (self.coords, self.size))

	def check_boundaries(self, screen_size):
		for i in [0, 1]:
			if (self.coords[i] < 0):
				self.coords[i] = 0
			elif (self.coords[i] >= screen_size[i] - self.size[i]):
				self.coords[i] = screen_size[i] - self.size[i]
	
	def has_collided(self, player):
		return ((self.coords[0] < player.coords[0] + player.size[0]) and
				(player.coords[0] < self.coords[0] + self.size[0]) and
				(self.coords[1] < player.coords[1] + player.size[1]) and
				(player.coords[1] < self.coords[1] + self.size[1]))

	def reset(self):
		self.coords = list(self.initial_coords)


WINDOW_SIZE = [200, 200]
PADDLE_SIZE = [5, 20]
BALL_SIZE = 5

paddle1 = Paddles(
	pygame.Color('white'),
	[0, 0],
	PADDLE_SIZE,
	5
)

paddle2 = Paddles(
	pygame.Color('magenta'),
	[200, 200],
	PADDLE_SIZE,
	5
)

ball = Ball(
	pygame.Color('red'),
	[100, 100],
	BALL_SIZE,
	5
)

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_UP]:
		paddle2.move('up')
	elif keys[pygame.K_DOWN]:
		paddle2.move('down')

	if keys[pygame.K_w]:
		paddle1.move('up')
	elif keys[pygame.K_s]:
		paddle1.move('down')

	paddle1.check_boundaries(WINDOW_SIZE)
	paddle2.check_boundaries(WINDOW_SIZE)

	window.fill(pygame.Color('black'))

	paddle1.draw(window)
	paddle2.draw(window)

	pygame.display.update()
	clock.tick(60)