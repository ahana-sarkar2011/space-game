import pygame
pygame.init()
bg = pygame.image.load("lesson 5-space game/images/space.png")
shootingsound = pygame.mixer.Sound("lesson 5-space game/images/Gun+Silencer.mp3")
collision = pygame.mixer.Sound("lesson 5-space game/images/Grenade+1.mp3")
WIDTH = 1000
HEIGHT = 600
redbullets = []
yellowbullets = []
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                shootingsound.play()
                bullet = pygame.Rect(red.x+30,red.y+30,10,10)
                redbullets.append(bullet)
            if event.key == pygame.K_RCTRL:
                shootingsound.play()
                bullety = pygame.Rect(yellow.x+30,yellow.y+30,10,10)
                yellowbullets.append(bullety)
    
    keys_pressed = pygame.key.get_pressed()
    redmove()
    yellowmove()
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(redss,red)
    yellowhealth = font.render("HEALTH = "+str(yellowh),True,"yellow")
    screen.blit(yellowss,yellow)
    redhealth = font.render("HEALTH = "+str(redh),True,"red")
    screen.blit(redhealth,(10,10))
    screen.blit(yellowhealth,(700,10))
    for bullet in redbullets:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x+=10
        if bullet.colliderect(yellow):
            redbullets.remove(bullet)
            yellowh -= 1
            collision.play()
    for bullety in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullety)
        bullety.x -= 10
        if bullety.colliderect(red):
            yellowbullets.remove(bullety)
            redh -= 1
            collision.play()
    if redh<1:
        ywins = font.render("YELLOW WINS",True,"yellow")
        screen.blit(ywins,(300,260))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    if yellowh<1:
        rwins = font.render("RED WINS",True,"red")
        screen.blit(rwins,(300,300))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    pygame.display.update()