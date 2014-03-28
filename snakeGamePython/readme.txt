Name: Shaheen Ghazazani
Class: COMP1405 - Patrick Morin
Date: Nov 14th, 2013
Assignment #8- Read me

Goal #1-> Brief description of how to play the game:

So once you run the file called pygame.py you will immediately be
greeted by a start screen with three options. As written on the
start screen move using arrows and hit enter to confirm your option.
The red highlighted option is the one your currently selecting.
If you hit exit game, the window is closed and game is exited. If
you hit instructons you will open a page with a more descriptive explanation
of the game as well as a button that will return you to the prior starting
sreen. The last option, hitting start grame will as you may have guessed, start
the game.

You now immediately take the role of a snake. Aimed downward in its original
direction you control its movement using arrow keys and must avoid smashing
into walls or your own tale!(basic snake concepts so far).

My added increments:
    there are multiple blocks. Red one will give you a bonus life, and is
    spawned on a increment timer of 15 seconds. The green block is always
    on your screen, it will appear again instantly if eaten and awards
    you 50 points. The 50 points can do multiple things explained below:
        How points work:
            1000 points, Congratulations you ate 20 blocks! lives + 1
            500 points, speeder reset. You're snake gets glued back
            together and its speed is reduced to base value.
            Whats the speeder?
            The speeder is a increment value that increases over time and is
            reset to put pressure and increase level of difficulty. So
            if you are taking alot of time getting to 500 points the snake
            will spread itself out slowly (as seen by seperated blocks) and
            it will increase its speed of movement making it harder to navigate.
            This speeder resets every 500 increment.
    Movement is simply controlled by only 4 keys, the arrow keys.
    Lives and score are demonstrated at the relative top right and left of the
    screen. Lives as said above increase via 1000 points, and red blocks. Points
    value on screen is reset at every 1000 to let you know how far you are from
    you're next life increase.

What happens during death?
You instantly respawn in the middle of the screen with the original downward
with reset speed value to avoid issues with instantly slamming into a wall.
You start with 4 lives, the one you currently commence the game with and 3
extra added in the lives remaining. Note: lives remaining will go to 0 as after
that death you have 0 lives remaining.

What remains through death?
-> Your score
-> The time increment for red blocks!(1 per 15seconds)

What doesnt remain through death?
-> Speed of your snake, it resets back to default
-> The length of your snake. It becomes reset

So at this point the only remaining thing is game finishing with 0 lifes
-> You are greeted with a game over screen strikingly similar to the start
screen (a pattern I found when investigating other games it seems they carry
        a similar template throughout)
-> You have 3 options. Read the instructions, Exit the game, Or restart which
all have the expected output, previously described above except for 'Restart Game'
which as you may have expected, instantly commences the snake game again with reset
score.

Goal #2-> How does this game satisfy all the requirements on assignment page:

1. Stick to resolution of 800x600.
Answer: Done deal-> I did.

2. Game should require some skill.
Answer: Reflexes and control, timing, speed. Moving the fast
snake into correct linear patterns is hard and requires pre-emptive
timing.

3. Game should have a maximum number of lives.
Answer: I have satisfied this through starting with four lives. Also
I have implemented the possibility of getting bonus lives.

4. The game should have a score that is displayed on the screen.
Answer: The score till the next live is present on the screen and
resets every 1000 which represents the next bonus live. The total
score is present summation at the game over screen.

5. Difficulty should increase as the game goes on.
Answer: The game has a speed based increment which makes the snake move
faster which resets every 500 points. As well as a 1 minute increment
timer which boots the snakes speed by a faster increment. Also as the game
goes on and on you eventually have such a long tail to control on a small screen
with the increased speed timers you're destined to die.

6. Input validation.
Answer: Game does not crash, ive tested hitting multiple keys on all pages.

7. The game should have sound effects.
Answer: Game has sound effects on game over, and start screen also
sound effects when the user hits enter selecting his option on both pages
above, as well as a sound effecting for changing options (up and down arrow).
Not to mention the looping music when the user is actually playing the game!

8. The game should have a sound track.
Answer: It does, as well as sound effects that are controlled using the
set volume function defined on the assignment page. 

9. The game should include start screen/ game over screen/ and pauses between lives.
Answer: Start screen/ Game over screen both implemented and since the period of
pause between lives is specific, I respawn the snake in the middle of the screen
and resets the speed which is the same pause available between hitting enter
to starting the game. This gives a never ending feeling, making it harder to
play the game.

10. Answer: I have to the best of my ability satiesfied all requirements
including the bonus. Proper background layering, making movement linear.
Making the split between speed increases linear. Although for this type of game
the option of moving like the ant is impossible since the ant does not move
linearly, rather on angles. Extra bling; Direct option to go from game over
to start game again, sound effects, etc.

Thanks for reading TA! I know it was a little extra long this time. Good luck
playing the game if you haven't! If you have, well thanks for spending that time.
- Shaheen Ghazazani (c)
^Yes I put a copyright symbol. 
