# Importing the Pygame Zero and random modules
import pgzrun
import random

# Set the size of the screen
WIDTH = 800
HEIGHT = 600

TITLE = '5 - Lists and Sounds'

# Set the background color
BGCOLOUR = (100, 100, 0)

FIRE_SPEED = 5

# Create the heath actor and place it at a random position
heath = Actor('heath', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Create the coin actor and place it at a random position
coin = Actor('coin', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Create the enemies list. This will hold all the fire actors
enemies = []

# Creates a fire actor, places it at a random x, sets direction and adds to enemies list
fire_1 = Actor('fire', (random.randint(0, WIDTH), 300))
fire_1.direction = (0, FIRE_SPEED)
enemies.append(fire_1)


def update():
    # Move the heath actor left or right if the left or right arrow keys are pressed
    if keyboard.left:
        heath.x -= 5
    if keyboard.right:
        heath.x += 5

    # Move the heath actor up or down if the up or down arrow keys are pressed
    if keyboard.up:
        heath.y -= 5
    if keyboard.down:
        heath.y += 5

    # Check for collision with the obstacle
    if heath.colliderect(coin):
        coin.x, coin.y = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    
    # TODO: Add code to stop Heath going off the screen

    # TODO: Add code to make the fire obstacles move - one side to side, thee other up and down


def draw():
    # Set the background color before drawing the actors
    screen.fill(BGCOLOUR)
    heath.draw()
    coin.draw()
    fire_1.draw()
    fire_2.draw()

pgzrun.go()
