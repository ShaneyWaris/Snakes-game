import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# colors
white = (255, 255, 255)
red   = (255, 0, 0)
black = (0, 0, 0)
blue = (0,0,255)
# Creating windows
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background image
bgimg = pygame.image.load("image.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("My First Python Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y) :
	screen_text = font.render(text, True, color)
	gameWindow.blit(screen_text, [x, y])
	
def plot_snake(gameWindow, color, snake_list, snake_size) :
	for x,y in snake_list :
		pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
		
def welcome():
	exit_game = False
	bgimg_2 = pygame.image.load("image2.jpg")
	bgimg_2 = pygame.transform.scale(bgimg_2, (screen_width, screen_height)).convert_alpha()
	pygame.display.update()
	while not exit_game :
		#gameWindow.fill((255,240,235))
		gameWindow.blit(bgimg_2, (0, 0))
		text_screen("Welcome to Snakes",black, 260, 250)
		text_screen("Press Space Bar To Play",black,230,290)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				exit_game = True
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_SPACE :
					pygame.mixer.music.load("background.mp3")
					pygame.mixer.music.play()
					gameloop()
			
		pygame.display.update()
		clock.tick(60)
		
def gameloop():
	# Game specific variables 
	exit_game = False
	game_over = False
	snake_x = 45
	snake_y = 55
	snake_size = 25
	fps = 50
	velocity_x = 0
	velocity_y = 0
	init_velocity = 4
	clock = pygame.time.Clock()
	food_x = random.randint(20, screen_width/2)
	food_y = random.randint(20, screen_height/2)
	score = 0
	snake_list = []
	snake_length = 1
	# check weither high score file is exist or not
	if (not os.path.exists("High_score.txt")):
		with open("High_score.txt","w") as f :
			f.write("0")
	with open("High_score.txt","r") as f :
		high_score = f.read()
	
	
	while not exit_game :
		if game_over :
			with open("High_score.txt","w") as f :
				f.write(str(high_score))
			gameWindow.fill(white)
			text_screen("Game Over!!!   Press Enter to Continue", black, 100, 250)
			
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					exit_game == True
					
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_RETURN :
						welcome()
			
		else :
			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					exit_game == True
				
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_RIGHT :
						velocity_x = init_velocity
						velocity_y = 0
					if event.key == pygame.K_LEFT :
						velocity_x =  -1 * init_velocity
						velocity_y = 0
					if event.key == pygame.K_UP :
						velocity_y = -1 * init_velocity 
						velocity_x = 0
					if event.key == pygame.K_DOWN :
						velocity_y = init_velocity
						velocity_x = 0
						
					if event.key == pygame.K_q :
						score += 10
						
			snake_x = snake_x + velocity_x
			snake_y = snake_y + velocity_y
			
			if abs(snake_x - food_x) < 18 and abs(snake_y - food_y) < 18 :
				score = score + 10
				food_x = random.randint(20, screen_width/2)
				food_y = random.randint(20, screen_height/2)
				snake_length += 4
				if score > int(high_score) :
					high_score = score
					
			gameWindow.fill(white)
			gameWindow.blit(bgimg, (0, 0))
			
			pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
			text_screen("Score : " + str(score) + "    High Score : " + str(high_score), blue, 5, 5)
			
			head = []
			head.append(snake_x)
			head.append(snake_y)
			snake_list.append(head)
			
			if len(snake_list) > snake_length :
				del snake_list[0]
				
			if head in snake_list[:-1] :
				game_over = True
				pygame.mixer.music.load("gameover.mp3")
				pygame.mixer.music.play()
			if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height :
				game_over = True
				pygame.mixer.music.load("gameover.mp3")
				pygame.mixer.music.play()
				
			plot_snake(gameWindow, black, snake_list, snake_size)
		pygame.display.update()
		clock.tick(fps)
		
	pygame.quit()
	quit()

welcome()