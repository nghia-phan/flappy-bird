import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption('flappy bird')
clock =pygame.time.Clock()

background_img = pygame.image.load('images/background.png')
background_img=pygame.transform.scale(background_img,(400,600))

x_bird=50
y_bird=350
bird = pygame.image.load('images/bird.png')
bird = pygame.transform.scale(bird,(40,40))

bird_drop=0
gravity=0.5

x_tube1=0
y_tube1=randint(100,400)
x_tube2=200
y_tube2=randint(100,400)
x_tube3=400
y_tube3=randint(100,400)

tube_speed=2
tube_width=50
tube_img=pygame.image.load('images/tube.png')

tube_rv=pygame.image.load('images/tube_op.png')
white = (255,255,255)

tub1_pass=False
tub2_pass=False
tub3_pass=False

run = True

score=0
RED=(255,0,0)
font=pygame.font.SysFont('san',20)

while run:
	clock.tick(60)
	screen.blit(background_img,(0,0))

# 			ong o tren
	tube1_img=pygame.transform.scale(tube_img,(tube_width,y_tube1))
	tube1=screen.blit(tube1_img,(x_tube1,0))

	tube2_img=pygame.transform.scale(tube_img,(tube_width,y_tube2))
	tube2=screen.blit(tube2_img,(x_tube2,0))

	tube3_img=pygame.transform.scale(tube_img,(tube_width,y_tube3))
	tube3=screen.blit(tube3_img,(x_tube3,0))

# 			ong o duoi
	tube1_rvimg=pygame.transform.scale(tube_rv,(tube_width,(600-y_tube1-100)))
	tube1_rv=screen.blit(tube1_rvimg,(x_tube1,(y_tube1+100)))

	tube2_rvimg=pygame.transform.scale(tube_rv,(tube_width,(600-y_tube2-100)))
	tube2_rv=screen.blit(tube2_rvimg,(x_tube2,(y_tube2+100)))

	tube3_rvimg=pygame.transform.scale(tube_rv,(tube_width,(600-y_tube3-100)))
	tube3_rv=screen.blit(tube3_rvimg,(x_tube3,(y_tube3+100)))
  
	screen.blit(bird,(x_bird,y_bird))

# 		chim roi
	y_bird+=bird_drop
	bird_drop+=gravity

	score_txt=font.render("Score:"+str(score),True,RED)
	screen.blit(score_txt,(5,5))
	# tube di chuyen
	x_tube1-=tube_speed
	x_tube2-=tube_speed
	x_tube3-=tube_speed

	# tao tube
	if x_tube1<-tube_width:
		x_tube1=550
		y_tube1=randint(100,400)
		tub1_pass=False
	elif x_tube2<-tube_width:
		x_tube2=550
		y_tube2=randint(100,400)
		tub2_pass=False
	elif x_tube3<-tube_width:
		x_tube3=550
		y_tube3=randint(100,400)
		tub3_pass=False

	# tinh diem
	if x_tube1+tube_width <= x_bird and tub1_pass==False:
		score+=1
		tub1_pass=True 
	elif x_tube2+tube_width <= x_bird and tub2_pass==False:
		score+=1
		tub2_pass=True
	elif x_tube3+tube_width <= x_bird and tub3_pass==False:
		score+=1
		tub3_pass=True
	
	# kiem tra va cham
	tubes=[tube1,tube2,tube3,tube1_rv,tube2_rv,tube3_rv]
	for tube in tubes:
		if screen.blit(bird,(x_bird,y_bird)).colliderect(tube):
			tube_speed=0
			bird_drop=0


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				bird_drop=0
				bird_drop=bird_drop-7
		if y_bird >= 600:
			# print('lose')
			pass
	pygame.display.flip()  