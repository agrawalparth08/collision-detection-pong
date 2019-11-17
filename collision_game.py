import pygame
import random
import time

#initial window setup
pygame.init()
max_width = 1000
max_height = 500
win = pygame.display.set_mode((max_width,max_height))
pygame.display.set_caption("Test Game")

#win counter
red_counter = 0
blue_counter = 0

#Fonts init
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render(str(red_counter) + ":" + str(blue_counter), False, (255, 255, 255))

#First Init coordinates 
x_red = 30
y_red = 50
x_blue = 950
y_blue = 50
width = 20
height = 60
vel = 15

#run done
run = True

#player initialisation
player_red = pygame.Rect(x_red,y_red,width,height)
player_blue = pygame.Rect(x_blue,y_blue,width,height)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    #Red Player Movement Key Mapping wasd
    if keys[pygame.K_a]:
        if x_red > 0:
            x_red -= vel

    if keys[pygame.K_d]:
        if x_red < max_width-width:
            x_red += vel

    if keys[pygame.K_w]:
        if y_red > 0 :
            y_red -= vel

    if keys[pygame.K_s]:
        if y_red < max_height-height:
            y_red += vel

    #Blue Player Movement Key Mapping up,down,left,right arrow keys
    if keys[pygame.K_LEFT]:
        if x_blue >= -20 :
            x_blue -= vel

    if keys[pygame.K_RIGHT]:
        if x_blue < max_width-width : 
            x_blue += vel

    if keys[pygame.K_UP]:
        if y_blue > 0 :
            y_blue -= vel

    if keys[pygame.K_DOWN]:
        if y_blue <max_height-height :
            y_blue += vel

    win.fill((0,0,0))  # Fills the screen with black

    #First movement screen render
    player_red = pygame.Rect(x_red,y_red,width,height)
    player_blue = pygame.Rect(x_blue,y_blue,width,height)
    pygame.draw.rect(win, (255,0,0), player_red)  
    pygame.draw.rect(win, (0,0,255), player_blue) 

    #If collision occurs, reset the player co-ordinates
    if player_red.colliderect(player_blue):
        x_red = 50
        y_red = random.randint(50,450)
        y_red  -= (y_red % 10)
        x_blue = 950
        y_blue = random.randint(50,450)
        y_blue -= (y_blue % 10)

    #Score String
    textsurface = myfont.render(str(red_counter) + ":" + str(blue_counter), False, (255, 255, 255))
    win.blit(textsurface,(max_width/2,max_height-50))
   
    #Winning Conditions
    if x_red >= max_width-width:
        print("RED WINS")
        myfont1 = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont1.render("RED WINS", False, (255, 255, 255))
        win.blit(textsurface,(max_width/2 - 50,0))
        red_counter += 1
        #reset the player coordinates
        x_red = 50
        y_red = random.randint(50,450)
        y_red  -= (y_red % 10)
        x_blue = 950
        y_blue = random.randint(50,450)
        y_blue -= (y_blue % 10)
        pygame.time.delay(1000) #delay in milliseconds
        win.fill((255,0,0))
         
    if x_blue <= -10:
        print("BLUE WINS")
        myfont1 = pygame.font.SysFont('Comic Sans MS', 60)
        textsurface = myfont1.render("BLUE WINS", False, (255, 255, 255))
        win.blit(textsurface,(max_width/2-50,0))
        blue_counter += 1
        #reset the player coordinates
        x_red = 50
        y_red = random.randint(50,450)
        y_red  -= (y_red % 10)
        x_blue = 950
        y_blue = random.randint(50,450)
        y_blue -= (y_blue % 10)
        pygame.time.delay(1000) #delay in milliseconds
        win.fill((0,0,255))

    pygame.draw.rect(win, (255,0,0), player_red)  
    pygame.draw.rect(win, (0,0,255), player_blue) 
    # print(x_red,y_red)
    # print(x_blue,y_blue)
    pygame.display.update()  

pygame.quit()