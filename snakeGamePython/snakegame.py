'''

Name: Shaheen Ghazazani

Class: Comp1405b

Date: Nov 11th, 2013

Assignment: Make a PYGAME A#8

Prof: Pat Morin

Due Date: Nov 18th, 2013

'''

# fix issue so snake can collide with itself and lose life

#currently raising a index error





from __future__ import division

import pygame, random, sys

from pygame.locals import *

import math





def collide(x1, x2, y1, y2, w1, w2, h1, h2):

    ''' check for collision of snake to prompt game over '''

    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:

        return True

    else:

        return False



class MyGame(object):

    def __init__(self):

        """Initialize a new game"""

        pygame.mixer.init()

        pygame.mixer.pre_init(44100, -16, 2, 2048)

        pygame.init()

        # set up a 640 x 480 window

        self.width = 800

        self.height = 600

        self.screen = pygame.display.set_mode((self.width, self.height))

        #setup positions

        self.xPosition = [290, 290, 290, 290, 290]

        self.yPosition = [290, 270, 250, 230, 210]

        #setup starting direction, apple position(green square) and certain variables for score

        #and for font, ect.

        self.life_death_timer = 0

        self.total_score = 0

        self.count_down_timer = 3

        self.speed_up_timer = 20

        self.box_timer = 0

        self.box_timer2 = 0

        self.counter = 0

        self.direction = 0

        self.current_score = 0

        self.live_reduce_counter = 0

        self.different_default = 0

        self.applepos = (random.randint(50, 590), random.randint(50, 590))

        pygame.display.set_caption('Feed The Snake!')

        self.appleimage = pygame.Surface((10, 10))

        (self.appleimage).fill((0, 255, 0))

        self.img = pygame.Surface((20, 20))

        (self.img).fill((255, 215, 0))

        self.myFont = pygame.font.Font('Ampad.ttf', 40)

        self.myFont2 = pygame.font.Font('Ampad.ttf', 45)

        self.clock = pygame.time.Clock()

        (self.redappleimage) = pygame.Surface((10, 10))

        (self.redappleimage).fill((255,0,0))

        self.redapplepos = (5000,5000)

        (self.blueappleimage) = pygame.Surface((10,10))

        (self.blueappleimage).fill((0,0,255))

        self.blueapplepos = (5000,5000)

        # Setup a timer to refresh the display FPS times per second

        self.lives = 3

        self.FPS = 30

        self.REFRESH = pygame.USEREVENT+1

        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)

        #chasing boolean

        self.chasing = True

        #fonts

        self.hit_enterimg2 = self.myFont.render('Hit Enter to Continue',True, (255,215,0))

        self.hit_enterimg = self.myFont.render('Wait 3 Seconds to Continue',True, (255,215,0))





    def run(self):

        running = True

        while running:

            event = pygame.event.wait()

            if event.type == QUIT:

                pygame.quit()

                sys.exit(0)

            elif event.type == KEYDOWN:

                if (event.key == K_UP or event.key == K_w)  and self.direction != 0:

                    self.direction = 2

                elif (event.key == K_DOWN or event.key == K_s) and self.direction != 2:

                    self.direction = 0

                elif (event.key == K_LEFT or event.key == K_a) and self.direction != 1:

                    self.direction = 3

                elif (event.key == K_RIGHT or event.key == K_d) and self.direction != 3:

                    self.direction = 1

                

            elif event.type == self.REFRESH:

                if (self.counter%210 == 0) and (self.counter != 0):

                    self.speed_up_timer += 2

                if (self.counter%3600 == 0) and (self.counter != 0):

                    self.different_default += 1

                    self.speed_up_timer += 5

                if (((self.current_score%500 == 0) or (self.current_score%600 ==0) \

                    or (self.current_score%550 == 0) or (self.current_score%650 == 0)) \

                   and (self.current_score != 0)):

                    self.speed_up_timer = 20

                if self.current_score != 0 and((self.current_score%1100 == 0) \

                    or (self.current_score%1000 == 0) or (self.current_score%1050 == 0) \

                                               or (self.current_score%1150 == 0)):

                    self.total_score += self.current_score #add to whole score

                    self.current_score = 0 #reset to 0 after adding

                    self.lives += 1 #give bonus of set value, this time being +1 lifes

                self.counter += 1

                self.box_timer += 1

                self.box_timer2 += 1

                self.draw()

            else:

                 pass

    def draw(self):

        i = len(self.xPosition)-1

        while i >= 2:

            if collide(self.xPosition[0], self.xPosition[i], self.yPosition[0], self.yPosition[i], 20,20,20,20):

                    #raise IndexError

                        #self.lives -= 1 

                if self.lives == 0:

                    if self.total_score != 0:

                        pygame.time.wait(2000)

                        x1 = self.total_score+self.current_score

                        GOver(x1).run()

                    if self.total_score == 0:

                        pygame.time.wait(2000)

                        GOver(self.current_score).run()

                elif self.lives != 0:

                    #setup positions

                    self.xPosition = [290, 290, 290, 290, 290]

                    self.yPosition = [290, 270, 250, 230, 210]

                    #setup starting direction, apple position(green square) and certain variables for score

                    #and for font, ect.

                    self.direction = 0

                    if self.different_default > 0:

                        self.speed_up_timer = 25

                    else:

                        self.speed_up_timer = 20

                    self.counter = 0

                    self.chasing = False

                    





            i -= 1



        if collide(self.xPosition[0], self.applepos[0], self.yPosition[0], self.applepos[1], 20, 10, 20, 10):

                self.current_score += 50

                self.xPosition.append(500)

                self.yPosition.append(500)

                self.applepos = (random.randint(50, 590),random.randint(50, 590))

            

        if collide(self.xPosition[0], self.redapplepos[0], self.yPosition[0], self.redapplepos[1], 20, 10, 20, 10):

                self.lives += 1

                self.xPosition.append(500)

                self.yPosition.append(500)

                self.redapplepos = (5000,5000)

                self.box_timer = 0

        if collide(self.xPosition[0], self.blueapplepos[0], self.yPosition[0], self.blueapplepos[1], 20, 10, 20, 10):

                self.current_score += 200

                self.xPosition.append(500)

                self.yPosition.append(500)

                self.blueapplepos = (5000,5000)

                self.box_timer2 = 0



        if self.xPosition[0] < 0 or self.xPosition[0] > 780 or self.yPosition[0] < 0 or self.yPosition[0] > 580:

            if self.lives == 0:

                if self.total_score != 0:

                    pygame.time.wait(2000)

                    x1 = self.total_score+self.current_score

                    GOver(x1).run()

                if self.total_score == 0:

                    pygame.time.wait(2000)

                    GOver(self.current_score).run()

            else:

                #setup positions back to normal

                self.xPosition = [290, 290, 290, 290, 290]

                self.yPosition = [290, 270, 250, 230, 210]

                #setup starting direction, apple position(green square) and certain variables for score

                #and for font, ect.

                if self.different_default > 0:

                    self.speed_up_timer = 25

                else:

                    self.speed_up_timer = 20

                self.counter = 0

                self.live_reduce_counter = 0

                self.chasing = False

                

    

        if self.chasing == False:

            (self.img).fill((0, 0, 0))

            self.life_death_timer += 1

            self.live_reduce_counter += 1

            if self.live_reduce_counter == 1:

                self.lives -= 1

                self.box_timer = 0

                self.box_timer2 = 0

            if (self.life_death_timer%90 == 0) and (self.life_death_timer != 0):

                self.show_wait_text = True

            event = pygame.event.wait()

            if event.type == KEYDOWN:

                if event.key == K_RETURN:

                    (self.img).fill((255, 215, 0))

                    self.chasing = True

                    

 

        i = len(self.xPosition)-1

        while i >= 1:

                self.xPosition[i] = self.xPosition[i-1]

                self.yPosition[i] = self.yPosition[i-1]

                i -= 1

        if self.chasing == True:

            if self.direction == 0:

                    self.yPosition[0] += self.speed_up_timer

            elif self.direction == 1:

                    self.xPosition[0] += self.speed_up_timer

            elif self.direction == 2:

                    self.yPosition[0] -= self.speed_up_timer

            elif self.direction == 3:

                    self.xPosition[0] -= self.speed_up_timer



        (self.screen).fill((0,0,0))



        for i in range(0, len(self.xPosition)):

                (self.screen).blit((self.img), (self.xPosition[i], self.yPosition[i]))

        (self.screen).blit(self.appleimage, self.applepos)

        if (self.box_timer%600 == 0) and (self.box_timer != 0):

            self.redapplepos = (random.randint(50,590), random.randint(50,590))

        if (self.redapplepos[0] != 5000 and self.redapplepos[1] != 5000):

            (self.screen).blit(self.redappleimage, self.redapplepos)

        if (self.box_timer2%360 == 0) and (self.box_timer2 != 0):

            self.blueapplepos = (random.randint(50,590), random.randint(50,590))

        if (self.blueapplepos[0] != 5000 and self.blueapplepos[1] != 5000):

            (self.screen).blit(self.blueappleimage, self.blueapplepos)

        the_score = (self.myFont2).render(('Total Score: '+ str(self.current_score + self.total_score)), True, (255,255,255))

        the_lives = (self.myFont).render(('Remaining Lives: '+str(self.lives)), True, (255,0,0))

        (self.screen).blit(the_score, (10, 10))

        (self.screen).blit(the_lives, (450,10))

        #(self.screen).blit(self.hit_enterimg, (200,330))

        if self.chasing == False:

            (self.screen).blit(self.hit_enterimg2, (200,330))

        pygame.display.flip()





class GOver(object):

    def __init__(self, score):

        self.score = score

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

        self.Author_Font2 = pygame.font.SysFont(None, 90)

        self.Header_Font = pygame.font.Font('Trocadero.ttf', 80)

        self.Title = (self.Header_Font).render(('GameOver'), True, (255,255,255))

        self.Points = (self.Author_Font2).render(('Total Score: %d' % (self.score)), True, (0,255,0))

        self.Start = (self.Start_Screen_Font).render(('Restart Game'), True, (255,255,255))

        self.Exit = (self.Start_Screen_Font).render(('Exit Game'), True, (255,255,255))

        self.Instructions = (self.Start_Screen_Font).render(('Instructions'), True, (255,255,255))

        self.Start_Instructions = (self.Author_Font).render(('Use arrow keys to move options, enter to select!'), True, (255,215,0))

        self.Author_Stamp = (self.Author_Font).render(('(C)Shaheen Ghazazani, Comp1405 Prof Pat Morin: Welcome all Players and TA\'s'), True, (255,215,0))

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

                        #Start_Screen().run()

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

        ((self.Start_Screen_Font).render(('Restart Game'), True, (255,0,0))) ]

        if self.direction == 2:

            self.Start = self.red_list[self.direction]

            self.Exit = (self.Start_Screen_Font).render(('Exit Game'), True, (255,255,255))

            self.Instructions = (self.Start_Screen_Font).render(('Instructions'), True, (255,255,255))

        if self.direction == 1:

            self.Exit = self.red_list[self.direction]

            self.Start = (self.Start_Screen_Font).render(('Restart Game'), True, (255,255,255))

            self.Instructions = (self.Start_Screen_Font).render(('Instructions'), True, (255,255,255))

        if self.direction == 0:

            self.Instructions = self.red_list[self.direction]

            self.Start = (self.Start_Screen_Font).render(('Restart Game'), True, (255,255,255))

            self.Exit = (self.Start_Screen_Font).render(('Exit Game'), True, (255,255,255))



        

        #output blit images make rect for actual png files and flip the display

        (self.screen).fill((0,0,0))

        (self.screen).blit(self.Points, (130, 450))

        (self.screen).blit(self.Title, (10,30))

        (self.screen).blit(self.Start, (10,200))

        (self.screen).blit(self.Exit, (10,250))

        (self.screen).blit(self.Instructions, (10,300))

        (self.screen).blit(self.Author_Stamp, (10, 570))

        (self.screen).blit(self.Start_Instructions, (10, 155))

        pygame.display.flip()





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

                        self.direction = 0

                elif event.key == K_DOWN:

                    self.option_chosen_music.play()

                    self.direction -= 1

                    if 0 > self.direction:

                        self.direction = 2

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





