import pgzrun
import random

# Set the size of the screen
WIDTH = 800
HEIGHT = 600

TITLE = '4 - Mouse Clicks'

BGCOLOUR = (255, 200, 0)

heath_speed = 5

# Create the heath actor and place it at a random position
heath = Actor('heath', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))
# Create the cross actor and place it off the screen
cross = Actor('cross', (-50, -50))

score = 0

def update():
    # Make Heath move randomly
    move_x = random.choice([heath_speed, -heath_speed])
    move_y = random.choice([heath_speed, -heath_speed])
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
    screen.fill(BGCOLOUR)
    heath.draw()
    cross.draw()
    # TODO: Draw the score

def on_mouse_down(pos):
    cross.pos = pos
    
    # TODO: Add code to check for collision with Heath. If there is a collision, increase the score by 1
    # and change the cross image to a tick. If there is not a collision, decrease the score by 1 and
    # make the cross image a cross.
    clock.schedule(hide_cross, 0.5)

def hide_cross():
    # This code moves the cross off screen after 0.5 seconds. 
    cross.pos = (-50, -50)

pgzrun.go()