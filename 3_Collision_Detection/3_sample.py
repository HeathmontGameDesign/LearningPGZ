import pgzrun
import random

# Set the size of the screen
WIDTH = 800
HEIGHT = 600

# Set the background color
BGCOLOUR = (100, 100, 190)

# Create the heath actor and place it at a random position
heath = Actor('heath', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Create the obstacle actor and place it at a random position
obstacle = Actor('obstacle', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))

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
    if heath.colliderect(obstacle):
        print("Collision detected!")
        obstacle.x, obstacle.y = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

def draw():
    # Set the background color before drawing the actors
    screen.fill(BGCOLOUR)
    heath.draw()
    obstacle.draw()

pgzrun.go()
