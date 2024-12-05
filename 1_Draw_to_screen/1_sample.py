import pgzrun

# Set the size of the screen and the Title
WIDTH = 800
HEIGHT = 600
TITLE = "1 - Drawing to the screen"

# Colours (RGB) - Constants
WHITE = (255, 255, 255)
RED = (180, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 170, 0)
YELLOW = (255, 255, 0)

def draw():
    # Set the background color to red
    screen.fill(RED)
    
    # Draw a white circle at the center of the screen
    screen.draw.circle((400, 300), 30, WHITE)

    # Draw a filled blue rectangle at the bottom of the screen
    screen.draw.filled_rect(Rect(0, 500, 800, 100),  BLUE)

    # Add a yellow line from the top left to the bottom right
    screen.draw.line((0, 0), (800, 600), YELLOW)

    #TODO: Add a filled in blue circle in the top right corner

    #TODO: Add a green rectangle that covers the left hand side of the screen
    

def update():
    # We don't actually need this for this example, but we would almost always use the update
    # function to update the state of the game, such as moving sprites, checking for collisions, etc.
    pass

pgzrun.go()