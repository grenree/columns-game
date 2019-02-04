import sys
sys.path.append("C:\Python36\Lib\site-packages")
import pygame
from faller import Faller


clock = pygame.time.Clock()

def check_events(settings,screen,faller):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,settings,screen,faller)
        if event.type == pygame.KEYUP:
            check_keyup_events(event,settings,screen,faller)

def check_keydown_events(event,settings,screen,faller):
    if event.key == pygame.K_q:
        pygame.quit()
        quit()
    elif event.key == pygame.K_RIGHT:
        faller[-1].move_right = True
    elif event.key == pygame.K_LEFT:
        faller[-1].move_left = True
    elif event.key == pygame.K_SPACE:
        faller[-1].fallerRotate()
        

def check_keyup_events(event,settings,screen,faller):
    if event.key==pygame.K_RIGHT:
        faller[-1].move_right = False
    elif event.key == pygame.K_LEFT:
        faller[-1].move_left = False




def update_screen(settings,screen,faller):
    screen.fill(settings.bg_color)
    for i in range(len(faller)):
        faller[i].blitme()
    
    
    pygame.display.flip()
    
    #print(clock.get_time())
