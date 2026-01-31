import pygame
pygame.init()
bg = pygame.image.load("lesson 5-space game/images/space.png")
WIDTH = 1000
HEIGHT = 600
redh = 10
font = pygame.font.SysFont("rockwell",40)
redhealth = font.render("HEALTH = "+str(redh),True,"red")
yellowh = 10
font = pygame.font.SysFont("rockwell",40)
yellowhealth = font.render("HEALTH = "+str(yellowh),True,"yellow")
border = pygame.Rect(500,1,4,600)
redss = pygame.image.load("lesson 5-space game/images/spaceship_red.png")
redss = pygame.transform.scale(redss,(60,60))
redss = pygame.transform.rotate(redss,90)
red = pygame.Rect(100,300,60,60)
yellowss = pygame.image.load("lesson 5-space game/images/spaceship_yellow.png")
yellowss = pygame.transform.scale(yellowss,(60,60))
yellowss = pygame.transform.rotate(yellowss,270)
yellow = pygame.Rect(900,300,60,60)
def redmove():
    if keys_pressed[pygame.K_w] and red.y>0:
        red.y-=5
    if keys_pressed[pygame.K_s] and red.y<550:
        red.y+=5
    if keys_pressed[pygame.K_a] and red.x>0:
        red.x-=5
    if keys_pressed[pygame.K_d] and red.x<460:
        red.x+=5
def yellowmove():
    if keys_pressed[pygame.K_UP] and yellow.y>0:
        yellow.y-=5
    if keys_pressed[pygame.K_DOWN] and yellow.y<550:
        yellow.y+=5
    if keys_pressed[pygame.K_LEFT] and yellow.x>500:
        yellow.x-=5
    if keys_pressed[pygame.K_RIGHT] and yellow.x<960:
        yellow.x+=5

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("dark blue")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    redmove()
    yellowmove()
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(redss,red)
    screen.blit(yellowss,yellow)
    screen.blit(redhealth,(10,10))
    screen.blit(yellowhealth,(700,10))
    pygame.display.update()