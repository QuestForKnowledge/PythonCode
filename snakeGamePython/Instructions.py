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
from homepage import *
import math



class Info_Screen2(object):
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
        self.Author_Font = pygame.font.SysFont(None, 25)
        self.Author_Font2 = pygame.font.SysFont(None, 33)
        self.Author_Font3 = pygame.font.SysFont(None, 40)
        self.Header_Font = pygame.font.Font('Trocadero.ttf', 100)
        self.inst1 = self.Author_Font.render('Move with arrows, eat the blocks that are green for points (+50 points per green)',True, (255,215,0))
        self.inst2 = self.Author_Font.render('by moving the snake over them. Eat read blocks for 500 points (+500 per red',True, (255,215,0))
        self.inst3 = self.Author_Font.render('500 points is 1/2 a life, once you reach 1000 points you get the score value reset',True, (255,215,0))
        self.inst4 = self.Author_Font.render('One extra life, which will be displayed to you. You have 4 lives starting the game',True, (255,215,0))
        self.inst5 = self.Author_Font.render('The life you start with along with 3 extras. Time based intervals will be used to',True, (255,215,0))
        self.inst6 = self.Author_Font.render('increase speed of snake and seperate the snake out(youll see individual blocks of the snake ',True, (255,215,0))
        self.inst7 = self.Author_Font.render('the farther the distance between blocks(seperation) the faster the snake will move and',True, (255,215,0))
        self.inst9 = self.Author_Font.render('view this as the difficulty increasing aspect of the game that makes it non normal. It is',True, (255,215,0))
        self.inst8 = self.Author_Font.render('as a race against the clock to reset the snake at 500 points. When reset occurs snake will reset',True, (255,215,0))
        self.inst10 = self.Author_Font2.render('Recap: Eat blocks for points, +1000p = new life, +500p = speed reset',True, (255,255,255))
        self.inst11 = self.Author_Font2.render('Values: 50 p per green, 500p per red. Goal: Win the most points.',True, (255,255,255))
        self.guidance = self.Author_Font3.render('Arrows Disabled: Hit Enter key To Return To Game Menu',True, (0,255,0))
        self.Back_Home = (self.Start_Screen_Font).render(('Back to Home'), True, (255,0,0))
        self.Start_Instructions = (self.Author_Font).render(('Use arrow keys to move options, enter to select!'), True, (255,215,0))
        self.Author_Stamp = (self.Author_Font).render(('(C)Shaheen Ghazazani, Comp1405 Prof Pat Morin: Welcome all Players and TA\'s'), True, (0,255,0))
        self.music = pygame.mixer.Sound('homepagemusic.wav')
        self.option_chosen_music = pygame.mixer.Sound('soundeffect2.wav')
        (self.music).set_volume(0.8)
        (self.option_chosen_music).set_volume(0.3)
        #starting direction using for helping user select options
        self.direction = 0
        #setup some counters
        self.counter = 0
        self.background = pygame.image.load('snakewallpaper.png')
        self.background2 = pygame.image.load('snakewallpaper2.png')
        
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
                elif event.key == K_DOWN:
                    self.option_chosen_music.play()
                elif event.key == K_RETURN:
                    self.option_chosen_music.play()
                    if self.direction == 0:
                        #run back to home page
                        Start_Screen().run()
            elif event.type == self.REFRESH:
                if (self.counter%50 == 0):
                    (self.music).play()

                self.counter += 1
                self.draw()
            else:
                 pass
    def draw(self):
        if self.direction == 0:
            self.Instructions = self.Back_Home
            
        #output blit images make rect for actual png files and flip the display
        (self.screen).fill((0,0,0))
        (self.screen).blit(self.background, (10,150))
        (self.screen).blit(self.background2, (500,185))
        (self.screen).blit(self.inst1, (10, 10))
        (self.screen).blit(self.inst2, (10, 30))
        (self.screen).blit(self.inst3, (10, 50))
        (self.screen).blit(self.inst4, (10, 70))
        (self.screen).blit(self.inst5, (10, 90))
        (self.screen).blit(self.inst6, (10, 110))
        (self.screen).blit(self.inst7, (10, 130))
        (self.screen).blit(self.inst9, (10,150))
        (self.screen).blit(self.inst8, (10, 170))
        (self.screen).blit(self.inst10, (10, 230))
        (self.screen).blit(self.inst11, (10, 250))
        (self.screen).blit(self.guidance, (10, 350))
        (self.screen).blit(self.Back_Home, (115,380))
        (self.screen).blit(self.Author_Stamp, (10, 580))
        pygame.display.flip()
        


