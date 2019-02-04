import sys
sys.path.append("C:\Python36\Lib\site-packages")
import pygame
import random
from pygame.sprite import Sprite
from block import Block
yellow = (255,255,255)

clock = pygame.time.Clock()
class Faller():
    def __init__(self,settings,screen):
        self.screen = screen
        self.seetings = settings

        self.blockOne = Block(settings,screen)
        self.blockTwo = Block(settings,screen)
        self.blockThree = Block(settings,screen)
        #self.Pos = [0,50,100,150,200,250]
        self.Pos = random.sample(set([0,50,100,150,200,250]),1)
        self.startPos = self.Pos[0]

        #using blocks to create individual classes
        self.blockOne.rect.x = self.startPos
        self.blockOne.rect.y = 0
        self.blockTwo.rect.x = self.startPos
        self.blockTwo.rect.y = -50
        self.blockThree.rect.x = self.startPos
        self.blockThree.rect.y = -100
        self.currentTime = 0
        self.time=0

        #movement flags
        self.move_right = False
        self.move_left = False

        #add some delay to falling/rotating
        self.move = True
        self.moveDown = True

        #bottom block pos
        self.bottomNum = 1

    

    def update(self,faller):
        
        self.canMove_left = True
        self.canMove_right = True
        #print(self.time)
        
        for i in range(len(faller)-1):
            if self.bottomNum == 1:
                    if self.blockOne.rect.x == faller[i].blockOne.rect.x + 50 and self.blockOne.rect.y == faller[i].blockOne.rect.y :
                        self.canMove_left = False
                    elif self.blockOne.rect.x == faller[i].blockTwo.rect.x + 50 and self.blockOne.rect.y == faller[i].blockTwo.rect.y :
                        self.canMove_left = False
                    elif self.blockOne.rect.x == faller[i].blockThree.rect.x + 50 and self.blockOne.rect.y == faller[i].blockThree.rect.y :
                        self.canMove_left = False
                        
                    if self.blockOne.rect.x == faller[i].blockOne.rect.x - 50 and self.blockOne.rect.y == faller[i].blockOne.rect.y :
                        self.canMove_right = False
                    elif self.blockOne.rect.x == faller[i].blockTwo.rect.x - 50 and self.blockOne.rect.y == faller[i].blockTwo.rect.y :
                        self.canMove_right = False
                    elif self.blockOne.rect.x == faller[i].blockThree.rect.x - 50 and self.blockOne.rect.y == faller[i].blockThree.rect.y :
                        self.canMove_right = False
                    
            elif self.bottomNum == 2:
                if self.blockTwo.rect.x == faller[i].blockOne.rect.x + 50 and self.blockTwo.rect.y == faller[i].blockOne.rect.y :
                    self.canMove_left = False
                elif self.blockTwo.rect.x == faller[i].blockTwo.rect.x + 50 and self.blockTwo.rect.y == faller[i].blockTwo.rect.y :
                    self.canMove_left = False
                elif self.blockTwo.rect.x == faller[i].blockThree.rect.x + 50 and self.blockTwo.rect.y == faller[i].blockThree.rect.y :
                    self.canMove_left = False

                if self.blockTwo.rect.x == faller[i].blockOne.rect.x - 50 and self.blockTwo.rect.y == faller[i].blockOne.rect.y :
                    self.canMove_right = False
                elif self.blockTwo.rect.x == faller[i].blockTwo.rect.x - 50 and self.blockTwo.rect.y == faller[i].blockTwo.rect.y :
                    self.canMove_right = False
                elif self.blockTwo.rect.x == faller[i].blockThree.rect.x - 50 and self.blockTwo.rect.y == faller[i].blockThree.rect.y :
                        self.canMove_right = False
                        
            elif self.bottomNum == 3:
                if self.blockThree.rect.x == faller[i].blockOne.rect.x + 50 and self.blockThree.rect.y == faller[i].blockOne.rect.y :
                    self.canMove_left = False
                elif self.blockThree.rect.x == faller[i].blockTwo.rect.x + 50 and self.blockThree.rect.y == faller[i].blockTwo.rect.y :
                    self.canMove_left = False
                elif self.blockThree.rect.x == faller[i].blockThree.rect.x + 50 and self.blockThree.rect.y == faller[i].blockThree.rect.y :
                    self.canMove_left = False

                if self.blockThree.rect.x == faller[i].blockOne.rect.x - 50 and self.blockThree.rect.y == faller[i].blockOne.rect.y :
                    self.canMove_right = False
                elif self.blockThree.rect.x == faller[i].blockTwo.rect.x - 50 and self.blockThree.rect.y == faller[i].blockTwo.rect.y :
                    self.canMove_right = False
                elif self.blockThree.rect.x == faller[i].blockThree.rect.x - 50 and self.blockThree.rect.y == faller[i].blockThree.rect.y :
                    self.canMove_right = False
            
        
        if self.move_right and self.blockOne.rect.x < 250  and self.canMove_right and self.moveDown:
            self.currentTime = self.time
            self.blockOne.rect.x = self.blockOne.rect.x + 50
            self.blockTwo.rect.x = self.blockTwo.rect.x + 50
            self.blockThree.rect.x = self.blockThree.rect.x + 50
            self.moveDown = False

        if self.move_left and self.blockOne.rect.x > 0 and  self.canMove_left and self.moveDown:
            self.currentTime = self.time
            self.blockOne.rect.x = self.blockOne.rect.x - 50
            self.blockTwo.rect.x = self.blockTwo.rect.x - 50
            self.blockThree.rect.x = self.blockThree.rect.x - 50
            self.moveDown = False

        if self.moveDown == False and self.time > self.currentTime + 500:
            self.moveDown = True
         

    def updateFall(self):
        self.time = pygame.time.get_ticks()
        
        
        if self.time%1000 == 0 and self.move:
            #print(self.time)
            
            self.blockOne.rect.y = self.blockOne.rect.y + 50
            self.blockTwo.rect.y = self.blockTwo.rect.y + 50
            self.blockThree.rect.y = self.blockThree.rect.y + 50
            self.move = False

        if self.move == False and self.time%1000 > 0:
            self.move = True
        
    def check_Death(self):
        if self.blockOne.rect.y < 0 or self.blockTwo.rect.y < 0 or self.blockTwo.rect.y < 0:
            pygame.quit()
            quit()
            

    def newFallerCheck(self,settings,screen,faller):
        if self.blockOne.rect.y == 600 or self.blockTwo.rect.y == 600 or self.blockThree.rect.y == 600:
            faller.append(Faller(settings,screen))
            pygame.time.delay(1000)
        else:
            for i in range(len(faller)-1):
                if self.bottomNum == 1:
                    if self.blockOne.rect.x == faller[i].blockOne.rect.x and self.blockOne.rect.y == faller[i].blockOne.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    elif self.blockOne.rect.x == faller[i].blockTwo.rect.x and self.blockOne.rect.y == faller[i].blockTwo.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    elif self.blockOne.rect.x == faller[i].blockThree.rect.x and self.blockOne.rect.y == faller[i].blockThree.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    
                elif self.bottomNum == 2:
                    if self.blockTwo.rect.x == faller[i].blockOne.rect.x and self.blockTwo.rect.y == faller[i].blockOne.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    elif self.blockTwo.rect.x == faller[i].blockTwo.rect.x and self.blockTwo.rect.y == faller[i].blockTwo.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    elif self.blockTwo.rect.x == faller[i].blockThree.rect.x and self.blockTwo.rect.y == faller[i].blockThree.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                elif self.bottomNum == 3:
                    if self.blockThree.rect.x == faller[i].blockOne.rect.x and self.blockThree.rect.y == faller[i].blockOne.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    elif self.blockThree.rect.x == faller[i].blockTwo.rect.x and self.blockThree.rect.y == faller[i].blockTwo.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    elif self.blockThree.rect.x == faller[i].blockThree.rect.x and self.blockThree.rect.y == faller[i].blockThree.rect.y - 50 :
                        self.check_Death()
                        faller.append(Faller(settings,screen))
                        pygame.time.delay(1000)
                    
            
            
        

    def fallerRotate(self):
        if self.bottomNum == 1:
            self.bottomNum = 2
        elif self.bottomNum == 2:
            self.bottumNum = 3
        elif self.bottomNum == 3:
            self.bottomnum = 1
        self.tempX = self.blockOne.rect.x
        self.tempY = self.blockOne.rect.y
        self.tempTwoX = self.blockTwo.rect.x
        self.tempTwoY = self.blockTwo.rect.y
        self.tempThreeX = self.blockThree.rect.x
        self.tempThreeY = self.blockThree.rect.y

        self.blockOne.rect.x = self.tempThreeX
        self.blockOne.rect.y = self.tempThreeY
        self.blockTwo.rect.x = self.tempX
        self.blockTwo.rect.y = self.tempY
        self.blockThree.rect.x = self.tempTwoX
        self.blockThree.rect.y = self.tempTwoY
        
           
        
        
        
        
        
        
    def blitme(self):
        self.blockOne.blitme()
        self.blockTwo.blitme()
        self.blockThree.blitme()
        

        
