import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#MAP: 1 is grass, 2 is brick
map = [[4, 3, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,0 ,1, 4],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,2 ,2, 2],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,2 ,1, 1],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0 ,0 ,2, 2],
       [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0 ,0 ,0, 1],
       [0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,3, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1]]
stone = pygame.image.load('stone.png') #load your spritesheet
brick = pygame.image.load('brick.png') #load your spritesheet
dirt = pygame.image.load('dirt.png') #load your spritesheet
Link = pygame.image.load('link.png') #load your spritesheet
Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
green = pygame.image.load('green.png') #load your spritesheet
#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
#p2
xpos1 = 500 #xpos of player
ypos1 = 200 #ypos of player
vx1 = 0 #x velocity of player
vy1 = 0 #y velocity of player
keys1 = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround1 = False #this variable stops gravity from pulling you down more when on a platform


#animation variables variables
frameWidth = 32
frameHeight = 48
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

frameWidth1 = 32
frameHeight1 = 48
RowNum1 = 0 #for left animation, this will need to change for other animations
frameNum1 = 0
ticker1 = 0
direction1 = DOWN

while not gameover:
    clock.tick(60) #FPS
   
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_w:
                keys[UP]=True
            elif event.key == pygame.K_a:
                keys[LEFT]=True
            elif event.key == pygame.K_d:
                keys[RIGHT]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_w:
                keys[UP]=False
            elif event.key == pygame.K_a:
                keys[LEFT]=False
            elif event.key == pygame.K_d:
                keys[RIGHT]=False
         

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        RowNum = 0
        direction = LEFT
    if keys1[LEFT]==True:
        vx1=-3
        RowNum1 = 0
        direction1 = LEFT
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
        RowNum = 1
        direction = RIGHT
    elif keys1[RIGHT] == True:
        vx1 = 3
        RowNum1 = 1
        direction1 = RIGHT
    #turn off velocity
    else:
        vx = 0
        vx1 = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        RowNum = 2
        isOnGround = False
        direction = UP
    if keys1[UP] == True and isOnGround1 == True: #only jump when on the ground
        vy1 = -8
        RowNum1 = 2
        isOnGround1 = False
        direction1 = UP
   
   
       
    xpos+=vx #update player xpos
    ypos+=vy
   
    xpos1+=vx1 #update player xpos
    ypos1+=vy1
   
   
    #COLLISION
   
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==2 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==3:
        isOnGround = True
        vy=0
       
    else:
        isOnGround = False
       
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==2 or map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==3:
        vy=0
       
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]==1 or map[int((ypos)/50)][int((xpos-10)/50)]==1)  and direction == LEFT:
        xpos+=3
    if (map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]==2 or map[int((ypos)/50)][int((xpos-10)/50)]==2)  and direction == LEFT:
        xpos+=3
    if (map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]==3 or map[int((ypos)/50)][int((xpos-10)/50)]==3)  and direction == LEFT:
        xpos+=3
    #right collision needed here
    if (map[int((ypos+frameHeight-10)/50)][int((xpos+30)/50)]==1 or map[int((ypos)/50)][int((xpos+10)/50)]==1)  and direction == RIGHT:
        xpos-=3
    if (map[int((ypos+frameHeight-10)/50)][int((xpos+30)/50)]==2 or map[int((ypos)/50)][int((xpos+10)/50)]==2)  and direction == RIGHT:
        xpos-=3
    if (map[int((ypos+frameHeight-10)/50)][int((xpos+30)/50)]==3 or map[int((ypos)/50)][int((xpos+10)/50)]==3)  and direction == RIGHT:
        xpos-=3
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=3
    if xpos<0:
        xpos+=3

   
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
       
        if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==2 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==3:
        isOnGround = True
        vy=0
       
    else:
        isOnGround = False
    #p2
    #bump your head, ouch!
    if map[int((ypos1)/50)][int((xpos1+frameWidth1/2)/50)]==1 or map[int((ypos1)/50)][int((xpos1+frameWidth1/2)/50)]==2 or map[int((ypos1)/50)][int((xpos1+frameWidth1/2)/50)]==3:
        vy1=0
       
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos1+frameHeight1-10)/50)][int((xpos1)/50)]==1 or map[int((ypos1)/50)][int((xpos1-10)/50)]==1)  and direction == LEFT:
        xpos+=3
    if (map[int((ypos1+frameHeight1-10)/50)][int((xpos1)/50)]==2 or map[int((ypos1)/50)][int((xpos1-10)/50)]==2)  and direction == LEFT:
        xpos+=3
    if (map[int((ypos1+frameHeight1-10)/50)][int((xpos1)/50)]==3 or map[int((ypos1)/50)][int((xpos1-10)/50)]==3)  and direction == LEFT:
        xpos+=3
    #right collision needed here
    if (map[int((ypos1+frameHeight1-10)/50)][int((xpos1+30)/50)]==1 or map[int((ypos1)/50)][int((xpos1+10)/50)]==1)  and direction == RIGHT:
        xpos-=3
    if (map[int((ypos1+frameHeight1-10)/50)][int((xpos1+30)/50)]==2 or map[int((ypos1)/50)][int((xpos1+10)/50)]==2)  and direction == RIGHT:
        xpos-=3
    if (map[int((ypos1+frameHeight1-10)/50)][int((xpos1+30)/50)]==3 or map[int((ypos1)/50)][int((xpos1+10)/50)]==3)  and direction == RIGHT:
        xpos-=3
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos1+frameWidth1 > 800:
        xpos1-=3
    if xpos1<0:
        xpos1+=3

   
    #stop falling if on bottom of game screen
    if ypos1 > 800-frameHeight:
        isOnGround1 = True
        vy1 = 0
        ypos1 = 800-frameHeight
   
    #gravity
    if isOnGround1 == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
   

       
    #ANIMATION-------------------------------------------------------------------
       
    # Update Animation Information

    if vx != 0: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>7:
           frameNum = 0
    if vx1 != 0: #animate when moving
        ticker1+=1
        if ticker1%10==0: #only change frames every 10 ticks
          frameNum1+=1
        if frameNum1>7:
           frameNum1 = 0
   
 
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
   
    #draw map
    for i in range (16):
        for j in range(16):
            if map[i][j]==1:
                screen.blit(dirt, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(stone, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==4:
                screen.blit(green, (j*50, i*50), (0, 0, 50, 50))
   
    screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    screen.blit(Link, (xpos1, ypos1), (frameWidth1*frameNum1, RowNum1*frameHeight1, frameWidth1, frameHeight1))
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()
