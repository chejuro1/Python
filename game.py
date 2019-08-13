import pygame
import random 
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600 

RED = (255,0,0)
BLUE = (0,0,255)
BACKGROUND_COLOR = (0,0,0)
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]
enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]

enemy_list = [enemy_pos]
screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False
speed =10
#clock = pygame.time.Clock
def drop_enemies(enemy_list):
    delay = random.random()
    if(len(enemy_list)< 10 ):
        x_pos = random.randint(0,WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])

def update_enemy_positions(enemy_list):
    for idx,enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += speed
        else:
            #enemy_pos[0] = random.randint(0,WIDTH-enemy_size)
            #enemy_pos[1] = 0
            enemy_list.pop(idx)
def collision_check(enemy_list):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
        return False

      

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen,BLUE,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

def detect_collision(play_pos,enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x <  (e_x + enemy_size)):
        if(e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x,y]

    screen.fill(BACKGROUND_COLOR)

    # update the position
    

    if detect_collision(player_pos,enemy_pos):
         game_over = true
         break

    drop_enemies(enemy_list)
    update_enemy_positions(enemy_list)

   # if collision_check(enemy_list):
     #   game_over = True
     #   break 

    draw_enemies(enemy_list)
    
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    
   # clock.tick(30)
    

    pygame.display.update()




