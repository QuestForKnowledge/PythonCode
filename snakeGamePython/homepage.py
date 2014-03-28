'''
Name: Shaheen Ghazazani
Class: Comp1405b
Date: Nov 11th, 2013
Assignment: Make a PYGAME A#8
Prof: Pat Morin
Due Date: Nov 18th, 2013
'''
from __future__ import division
import pygame, random, sys
from pygame.locals import *
#from snakegame import *
import math



class Start_Screen(object):
    def __init__(self):
        """Initialize a new game"""
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        # set up a 640 x 480 window
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        #setup font and overall text on screen as well as images and sounds all below
        self.Start_Screen_Font = pygame.font.Font('barricade.ttf', 60)
        self.Author_Font = pygame.font.SysFont(None, 30)
        self.Header_Font = pygame.font.Font('Trocadero.ttf', 100)
        self.Title = (self.Header_Font).render(('Snake V2'), True, (255,255,255))
        self.Start = (self.Start_Screen_Font).render(('Start Game'), True, (255,255,255))
        self.Exit = (self.Start_Screen_Font).render(('Exit Game'), True, (255,255,255))
        self.Instructions = (self.Start_Screen_Font).render(('Instructions'), True, (255,255,255))
        self.Start_Instructions = (self.Author_Font).render(('Use arrow keys to move options, enter to select!'), True, (255,215,0))
        self.Author_Stamp = (self.Author_Font).render(('(C)Shaheen Ghazazani, Comp1405 Prof Pat Morin: Welcome all Players and TA\'s'), True, (255,215,0))
        self.background = pygame.image.load('snakewallpaper.png')
        self.background2 = pygame.image.load('snakewallpaper2.png')
        self.music = pygame.mixer.Sound('homepagemusic.wav')
        self.option_chosen_music = pygame.mixer.Sound('soundeffect2.wav')
        (self.music).set_volume(0.8)
        (self.option_chosen_music).set_volume(0.3)
        #starting direction using for helping user select options
        self.direction = 2
        #setup some counters
        self.counter = 0
        
        # Setup a timer to refresh the display FPS times per second
        self.FPS = 30
        self.REFRESH = pygame.USEREVENT+1
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)
    def run(self):
        running = True
        while running:
            
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.option_chosen_music.play()
                    self.direction += 1
                    if self.direction > 2:
                        self.direction = 2
                elif event.key == K_DOWN:
                    self.option_chosen_music.play()
                    self.direction -= 1
                    if 0 > self.direction:
                        self.direction = 0
                elif event.key == K_RETURN:
                    self.option_chosen_music.play()
                    if self.direction == 2:
                        #run other file to commence game
                        MyGame().run()
                    elif self.direction == 1:
                        pygame.quit()
                        sys.exit(0)
                    elif self.direction == 0:
                        #run file with instructions
                        Info_Screen2().run()
            elif event.type == self.REFRESH:
                if (self.counter%50 == 0):
                    (self.music).play()

                self.counter += 1
                self.draw()
            else:
                 pass
    def draw(self):
        self.red_list = [ \
        ((self.Start_Screen_Font).render(('Instructions'), True, (255,0,0))),
        ((self.Start_Screen_Font).render(('Exit Game'), True, (255,0,0))),
        ((self.Start_Screen_Font).render(('Start Game'), True, (255,0,0))) ]
        if self.direction == 2:
            self.Start = self.red_list[self.direction]
            self.Exit = (self.Start_Screen_Font).render(('Exit Game'), True, (255,255,255))
            self.Instructions = (self.Start_Screen_Font).render(('Instructions'), True, (255,255,255))
        if self.direction == 1:
            self.Exit = self.red_list[self.direction]
            self.Start = (self.Start_Screen_Font).render(('Start Game'), True, (255,255,255))
            self.Instructions = (self.Start_Screen_Font).render(('Instructions'), True, (255,255,255))
        if self.direction == 0:
            self.Instructions = self.red_list[self.direction]
            self.Start = (self.Start_Screen_Font).render(('Start Game'), True, (255,255,255))
            self.Exit = (self.Start_Screen_Font).render(('Exit Game'), True, (255,255,255))

        
        #output blit images make rect for actual png files and flip the display
        (self.screen).fill((0,0,0))
        (self.screen).blit(self.background, (10,150))
        (self.screen).blit(self.background2, (500,185))
        (self.screen).blit(self.Title, (10,30))
        (self.screen).blit(self.Start, (175,300))
        (self.screen).blit(self.Exit, (175,350))
        (self.screen).blit(self.Instructions, (175,400))
        (self.screen).blit(self.Author_Stamp, (10, 570))
        (self.screen).blit(self.Start_Instructions, (10, 155))
        pygame.display.flip()
        

Start_Screen().run()

