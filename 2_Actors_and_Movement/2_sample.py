import pgzrun


# Set the size of the screen
WIDTH = 800
HEIGHT = 600

# Set the background color
BGCOLOUR = (0, 0, 160)

# Define the player actor and put it in the middle of the screen
player = Actor('heath', (WIDTH // 2, HEIGHT // 2))

def update():
    # Move the player left or right if the left or right arrow keys are pressed
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    # TODO: Add code to move the player up or down if the up or down arrow keys are pressed


def draw():
    # Set the background color before drawing the player
    screen.fill(BGCOLOUR)
    player.draw()

pgzrun.go()