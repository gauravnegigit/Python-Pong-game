import pygame
pygame.font.init()

#screen variables
WIDTH,HEIGHT = 1000 , 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PONG GAME USING PYGAME MODULE !")
FPS = 60

# game variables
left = pygame.Rect(100,200,50,200)
right = pygame.Rect(WIDTH - 150 ,200,50,200)
left_score,right_score = 0,0

#color variables
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#font variables
SCORE_FONT = pygame.font.SysFont("Arial Black",30)

def redraw(ball_x,ball_y):
	WIN.fill(GREEN)
	pygame.draw.rect(WIN,BLACK,left)
	pygame.draw.rect(WIN,BLACK,right)
	pygame.draw.circle(WIN,BLUE,(ball_x,ball_y),15)
	text = SCORE_FONT.render("LEFT PLAYER : "+str(left_score)+ "  RIGHT PLAYER : "+str(right_score),1,BLUE)
	WIN.blit(text,(WIDTH//2 - text.get_width()//2,10))
	pygame.display.update()

def main():
	global left_score,right_score
	run = True
	ball_x,ball_y = WIDTH//2 , HEIGHT//2
	dx,dy = 10,10
	clock = pygame.time.Clock()
	while run :
		clock.tick(FPS)
		redraw(ball_x,ball_y)
		ball_x += dx
		ball_y += dy
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_UP] and right.y >0:
			right.y -=20
		if keys_pressed[pygame.K_DOWN] and right.y < HEIGHT - right.height:
			right.y +=20
		if keys_pressed[pygame.K_w] and left.y>0:
			left.y -=20
		if keys_pressed[pygame.K_s] and left.y < HEIGHT - left.height:
			left.y += 20

		if ball_y<30 or ball_y > HEIGHT - 30:
			dy *= -1
		if ball_x < 30 :
			right_score +=10
			ball_x,ball_y = 500,300
		if ball_x > WIDTH - 30:
			left_score +=10
			ball_x,ball_y =500,300

		if 0<ball_x-left.x <65 and 0<ball_y-left.y<215:
			dx *= -1
		if 0<right.x - ball_x <35 and 0<ball_y-right.y<215:
			dx *= -1

if __name__ == '__main__':
	main()