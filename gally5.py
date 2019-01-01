import pygame
import numpy as np

pygame.init()
res = (1280, 720)
gally_upscaling_factor = 3
arrow_upscaling_factor = 3

display = pygame.display.set_mode(res, pygame.RESIZABLE)
pygame.display.set_caption("Gally escapes")

background = pygame.transform.smoothscale(pygame.image.load("background.png").convert(), res)

gally_normal = pygame.image.load("gally_normal.png").convert()
gally_size = gally_normal.get_size()
gally_normal.set_colorkey((0,0,0))
gally_normal = pygame.transform.smoothscale(gally_normal, (gally_size[0]*gally_upscaling_factor, gally_size[1]*gally_upscaling_factor))

gally_stepping = pygame.image.load("gally_stepping.png").convert()
gally_stepping = pygame.transform.smoothscale(gally_stepping, (gally_size[0]*gally_upscaling_factor, gally_size[1]*gally_upscaling_factor))
gally_stepping.set_colorkey((0,0,0))

gally_stepping2 = pygame.image.load("gally_stepping2.png").convert()
gally_stepping2 = pygame.transform.smoothscale(gally_stepping2, (gally_size[0]*gally_upscaling_factor, gally_size[1]*gally_upscaling_factor))
gally_stepping2.set_colorkey((0,0,0))

arrow2 = pygame.image.load("arrow2.png").convert()
arrow_size = arrow2.get_size()
arrow2 = pygame.transform.smoothscale(arrow2, (arrow_size[0]*arrow_upscaling_factor, arrow_size[1]*arrow_upscaling_factor))
arrow_size = arrow2.get_size()
arrow2.set_colorkey((0,0,0))


arrow = pygame.transform.flip(arrow2, True, False)



#arrow2.set_colorkey((0,0,0))

stage_1 = [None] * 6

gally = gally_normal
gally_x = 100
gally_y = 300
gally_goal = [None] * 6
gally_facing_right = False
gally_step_count = 0
step_size = 3
walking = False

clock = pygame.time.Clock()

display.blit(background, (0, 0))
pygame.display.update()

pressed_left, pressed_right = False,False

def mirror():
    global gally_stepping, gally_stepping2, gally_normal
    gally_stepping = pygame.transform.flip(gally_stepping, True, False)
    gally_stepping2 = pygame.transform.flip(gally_stepping2, True, False)
    gally_normal = pygame.transform.flip(gally_normal, True, False)


def in_range(a, b, limit = 2):
    if(abs(a-b)<=limit):
        return True
    else:
        return False

def set_walk(pos):
    global gally_x, gally_y, walking, gally_goal
    walking = True
    gally_goal[4] = pos[0]
    gally_goal[5] = pos[1]
    x_dif = pos[0]-gally_x
    y_dif = pos[1]-gally_y
    
    if x_dif < 0:
        #to the left
        gally_goal[0]=-1
    else:
        #to the right or nothing
        gally_goal[0]=1

    if y_dif < 0:
        #up
        gally_goal[1]=-1
    else:
        #down or nothing
        gally_goal[1]=1
    

while True:


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            set_walk(pos)
            
        if event.type == pygame.KEYDOWN:          # check for key presses          
            if event.key == pygame.K_LEFT:        # left arrow turns left
                pressed_left = True
            elif event.key == pygame.K_RIGHT:     # right arrow turns right
                pressed_right = True
        elif event.type == pygame.KEYUP:            # check for key releases
            if event.key == pygame.K_LEFT:        # left arrow turns left
                pressed_left = False
            elif event.key == pygame.K_RIGHT:     # right arrow turns right
                pressed_right = False

    clock.tick(40)
    display.blit(background, (0,0))

    arrow_offset_from_edge = 3
    display.blit(arrow2, (res[0]-arrow_size[0]-arrow_offset_from_edge,(res[1]-arrow_size[1])/2))
    display.blit(arrow, (arrow_offset_from_edge,(res[1]-arrow_size[1])/2))

    
    display.blit(gally, (gally_x-gally_size[0],gally_y-gally_size[1]*2))
            
    if walking:

        gally_step_count +=1

        if (not in_range(gally_x, gally_goal[4])):
            gally_x += (step_size*gally_goal[0])
            
        if (not in_range(gally_y, gally_goal[5])):
            gally_y += (step_size*gally_goal[1])
            
        if gally_goal[0] == -1:
            if gally_facing_right:
                mirror()
                gally_facing_right = gally_facing_right = False               

        else:
            if not gally_facing_right:
                mirror()
                gally_facing_right = gally_facing_right = True

        if in_range(gally_x, gally_goal[4]) and  in_range(gally_y, gally_goal[5]):
            walking = False

            
        if gally_step_count == 10:
            gally = gally_stepping
        elif gally_step_count == 20:
            gally = gally_normal
        elif gally_step_count == 30:
            gally = gally_stepping2
        if gally_step_count == 40:
            gally = gally_normal
            gally_step_count = 0
        

    pygame.display.flip()
















