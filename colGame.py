import sys
sys.path.append("C:\Python36\Lib\site-packages")

import pygame
from settings import Settings
import logic as gl
from faller import Faller

clock = pygame.time.Clock()
def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Columns")
    
    
    faller = []
    faller.append(Faller(settings,screen))


    while True:
        gl.check_events(settings,screen,faller)
        faller[-1].update(faller)
        faller[-1].updateFall()
        
            
            
        gl.update_screen(settings,screen,faller)
        faller[-1].newFallerCheck(settings,screen,faller)
        

run_game()
