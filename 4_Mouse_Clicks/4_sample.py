import pgzrun
import random

# Set the size of the screen
WIDTH = 800
HEIGHT = 600

TITLE = '4 - Mouse Clicks'

BGCOLOUR = (255, 200, 0)

HEATH_SPEED = 20

# GLOBAL VARIABLES
# Create the heath actor and place it at a random position
heath = Actor('heath', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))
# Create the cross actor and place it off the screen
cross = Actor('cross', (-50, -50))

score = 0

def update():
    # Because we want to use a simple variable (score) across multiple functions, we need to declare it as global
    global score
    # Heath moves HEATH_SPEED pixels in a random direction
    move_x = random.choice([HEATH_SPEED, -HEATH_SPEED])
    move_y = random.choice([HEATH_SPEED, -HEATH_SPEED])
    heath.x += move_x
    heath.y += move_y

    # If Heath goes off the screen, move him back to somewhere random
    if heath.left < 0:
        heath.left = random.randint(0, WIDTH)
    if heath.right > WIDTH:
        heath.right = random.randint(0, WIDTH)
    if heath.top < 0:
        heath.top = random.randint(0, HEIGHT)
    if heath.bottom > HEIGHT:
        heath.bottom = random.randint(0, HEIGHT)

def draw():
    # As above, score is being used as a global variable
    global score

    screen.fill(BGCOLOUR)
    heath.draw()
    cross.draw()
    # TODO: Draw the score

def on_mouse_down(pos):
    # Set the position of the cross to the position of the mouse click
    cross.pos = pos
    
    # TODO: Add code to check for collision with Heath. If there is a collision, increase the score by 1
    # and change the cross image to a tick. If there is not a collision, decrease the score by 1 and
    # make the cross image a cross.
    
    # This schedules the "hide_cross" function to run in 0.5 seconds, so that the cross doesn't stay on the screen.
    clock.schedule_unique(hide_cross, 0.5)

# hide_cross moves the cross off the screen
def hide_cross():
    cross.pos = (-50, -50)

pgzrun.go()