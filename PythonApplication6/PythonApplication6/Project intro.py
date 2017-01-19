# Copyright 2017
# Simon de Bakker, Raoul van Duivenvoorde, Jeroen de Schepper

import pygame
from pygame.locals import*
import sys
import math

class Application:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.size = (self.width, self.height)
    
        # Start PyGame
        pygame.init()
    
        # Set the resolution
        self.screen = pygame.display.set_mode((self.size))#, pygame.FULLSCREEN)
    
        self.phase = "intro"

        self.intro = Intro(self, self.width, self.height)
        self.game = Game(self, self.width, self.height)
        self.highscore = Highscore(self, self.width, self.height)
        self.tutorial = Tutorial(self, self.width, self.height)

    def back(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.application.phase = "intro"

    def application_loop(self):
        while not process_events():
            if self.phase == "intro":
                self.intro.draw(self.screen)
            elif self.phase == "game":
                self.game.draw(self.screen)
            elif self.phase == "pause":
                self.pause.draw(self.screen)
            elif self.phase == 'Highscore':
                self.highscore.draw(self.screen) 
            elif self.phase == 'Tutorial':
                self.tutorial.draw(self.screen)
            # Flip the screen
            pygame.display.flip()

class Intro:
    def __init__ (self, application, width, height):
        self.application = application
        self.Background = pygame.image.load("BackgroundA.jpg") #easteregg
        self.Background = pygame.transform.scale(self.Background, (width, height))
        self.font = pygame.font.SysFont('Arial', 150)
        self.exit_button = Button(self.application, 'Exit', (width/15), (height/1.25), 170, 50)
        self.tutorial_button = Button(self.application, 'Tutorial', (width/15), (height/1.4), 170, 50)
        self.highscore_button = Button(self.application, 'Highscore', (width/15), (height/1.6), 170, 50)
        self.start_button = Button(self.application, 'Start', (width/15), (height/1.86), 170, 50)
        self.width = width
        self.height = height
    def draw (self, screen):
        screen.blit(self.Background,(0, 0))
        title_text = self.font.render("BattlePort", 1, (255,120,0))
        screen.blit(title_text,((self.width / 15) , (self.height / 9)))
        self.exit_button.draw(screen)
        self.tutorial_button.draw(screen)
        self.highscore_button.draw(screen)
        self.start_button.draw(screen)

class Button:
    def __init__(self, application, text, x, y, w, h):
        self.application = application
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.surface = pygame.Surface((w, h))
        self.font = pygame.font.Font(None, 45)
    def draw (self, screen):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.x + 170 > mouse_pos[0] > self.x and self.y + 50 > mouse_pos[1] > self.y:
            screen.blit(self.surface, (self.x, self.y))
            button_text = self.font.render(self.text, 1, (255,255,255))
            screen.blit(button_text,(( self.x + 5), (self.y + 11)))
            if mouse_click[0]:
                print (self.text)
                if self.text == 'Start':
                    self.application.phase = "game"
                elif self.text == 'Pause':
                    self.application.phase = "pause"
                elif self.text == 'Tutorial':
                    self.application.phase = 'Tutorial'
                elif self.text == 'Highscore':
                    self.application.phase = "Highscore"
                elif self.text == 'Exit':
                    sys.exit()
        else:
            screen.blit(self.surface, (self.x, self.y))
            button_text = self.font.render(self.text, 1, (255,120,0))
            screen.blit(button_text,((self.x + 5), (self.y + 11)))

class Game:
    def __init__ (self, application, width, height):
        self.pause = Pause
        self.surface = pygame.Surface((width, height))
        self.application = application
        self.Background = pygame.image.load("Speelbord.png")
        self.Background = pygame.transform.scale(self.Background, (width, height))
        self.font = pygame.font.SysFont('Arial', 150)
        self.width = width
        self.height = height
        
        self.Ship1Move = Button(self.application, '', (width/70), (height/22.80), 55, 55)
        self.Ship1Def  = Button(self.application, '', (width/70), (height/7.300), 55, 55)
        self.Ship1Att  = Button(self.application, '', (width/70), (height/4.300), 55, 55)

        self.Ship2Move = Button(self.application, '', (width/70), (height/2.580), 55, 55)
        self.Ship2Def  = Button(self.application, '', (width/75), (height/2.075), 55, 55)
        self.Ship2Att  = Button(self.application, '', (width/75), (height/1.739), 55, 55)

        self.Ship3Move = Button(self.application, '', (width/75), (height/1.395), 55, 55)
        self.Ship3Def  = Button(self.application, '', (width/75), (height/1.233), 55, 55)
        self.Ship3Att  = Button(self.application, '', (width/75), (height/1.105), 55, 55)

        self.Yes = Button(self.application, 'Yes', (self.width/50), (self.height/22.80), 55, 55)
        self.No  = Button(self.application, 'No', (self.width/50), (self.height/7.300), 55, 55)

    def draw (self, screen):
        screen.blit(self.Background, (0,0))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            Pause.draw(self, screen)
        
class Pause:
    def __init__ (self, application, width, height):
        self.application = application
        self.width = width
        self.height = height
        
    def draw(self, screen):
        self.Yes.draw(screen)
        self.No.draw(screen)  
        
class Highscore:
    def __init__ (self, application, width, height):
        self.application = application
        self.Background = pygame.image.load("BackgroundA.jpg")
        self.Background = pygame.transform.scale(self.Background, (width, height))
        self.font = pygame.font.SysFont('Arial', 150)
        self.width = width
        self.height = height 
    def draw (self, screen):
        screen.blit(self.Background,(0,0))
        title_text = self.font.render("Highscore", 1, (255,120,0))
        screen.blit(title_text,((self.width / 15) , (self.height / 9)))
        Application.back(self)
    
class Tutorial:
    def __init__ (self, application, width, height):
        self.application = application
        self.Background = pygame.image.load("BackgroundA.jpg")
        self.Background = pygame.transform.scale(self.Background, (width, height))
        self.font = pygame.font.SysFont('Arial', 150)
        self.width = width
        self.height = height 
    def draw (self, screen):
        screen.blit(self.Background,(0,0))
        title_text = self.font.render("Tutorial", 1, (255,120,0))
        screen.blit(title_text,((self.width / 15) , (self.height / 9)))
        Application.back(self)
          
                
# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()

# Main program logic
def program():
    application = Application()
    application.application_loop()

# Start the program
program()
