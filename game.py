import random
from math import sqrt
from math import pow
import pygame
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((1024,600))
#displaying caption and icon
pygame.display.set_caption("alpha")
icon=pygame.image.load("my.png")
pygame.display.set_icon(icon)
#loading background
bg=pygame.image.load("m4.jpg")
#bgm
mixer.music.load("bgm.mp3")
mixer.music.play(-1)
#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
def show_score(x,y):
    score=font.render("score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
#player
hero=pygame.image.load("ns.png")
player_x=400
player_y=300
def player(x,y):
    screen.blit(hero,(x,y))
px=0
py=0
#enemy
ene=[]
enemy_x=[]
enemy_y=[]
ey=[]
enum=6
for i in range(enum):
    ene.append(pygame.image.load("s.png"))
    enemy_x.append(random.randrange(0,994,20))
    enemy_y.append(-10)
    ey.append(0)
def enemy(x,y,i):
    screen.blit(ene[i],(x,y))


#bullet
bullet_state="ready"
bullet_x=0
bullet_y=player_y
bullet=pygame.image.load("bull.png")
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x,y-7))
#colliding
def iscollide(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=sqrt(pow(bullet_x-enemy_x,2)+pow(bullet_y-enemy_y,2))
    
    if(distance<=27):
        return True
    else:
        return False
#player enemy distance
def ped(player_x,player_y,enemy_x,enemy_y):
    dis=sqrt(pow(enemy_x-player_x,2)+pow(enemy_y-player_y,2))
    return dis
#game over text
over_font=pygame.font.Font("freesansbold.ttf",65)
def game_over_text():
    over_text=over_font.render("game over",True,(245,\
                                                 25,155))
    screen.blit(over_text,(320,300))
running=True
while running:
    
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running=False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                px=px-5
            if(event.key == pygame.K_RIGHT):
                px=5
            if(event.key == pygame.K_UP):
                py=py-5
            if(event.key == pygame.K_DOWN):
                py=5
            if(event.key == pygame.K_SPACE):
                if(bullet_state=="ready"):
                    bullet_sound=mixer.Sound("fired.wav")
                    bullet_sound.play()
                    bullet_y=player_y
                    bullet_x=player_x
                    fire_bullet(bullet_x,bullet_y)
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                px=0
                py=0
    #player movement
    player_x=player_x+px
    player_y=player_y+py
    if(player_x<=0):
        player_x=0
    elif(player_x>=994):
        player_x=994
    elif(player_y<=0):
        player_y=0
    elif(player_y>=570):
        player_y=570
    #bullet movement
    if(bullet_y<=0):
        bullet_state="ready"
    if(bullet_state=="fire"):
        fire_bullet(bullet_x,bullet_y)
        bullet_y=bullet_y-6
    #enemy movement
    for i in range(enum):
        if(enemy_y[i]==2000):
            game_over_text()
            break
        dist=ped(player_x,player_y,enemy_x[i],enemy_y[i])
        if(dist<=20):
            for j in range(enum):
                enemy_y[j]=2000
            game_over_text()
            break
        if(enemy_y[i]<=0):
            ey[i]=4
            enemy_y[i]=enemy_y[i]+ey[i]
        elif(enemy_y[i]>=570):
            ey[i]=-4
            enemy_y[i]=enemy_y[i]+ey[i]
        enemy_y[i]=enemy_y[i]+ey[i]
        #collision
        collide=iscollide(enemy_x[i],enemy_y[i],bullet_x,bullet_y)
        if collide:
            collide_sound=mixer.Sound("hit.wav")
            collide_sound.play()
            bullet_y=player_y
            score_value=score_value+1
            bullet_state="ready"
            enemy_x[i]=random.randint(0,994)
            enemy_y[i]=-10
        enemy(enemy_x[i],enemy_y[i],i)
 
    
    
    player(player_x,player_y)
    show_score(textx,texty)
    pygame.display.update() 
    
