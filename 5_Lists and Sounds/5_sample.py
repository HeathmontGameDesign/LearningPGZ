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

# Set the number of frames before a new enemy is created. Set it low to test, high to play
NEW_FIRE_AFTER = 500

game_state = 'PLAYING'

# Create the heath actor and place it at a random position
heath = Actor('heath', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Create the coin actor and place it at a random position
coin = Actor('coin', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Create the enemies list. This will hold all the fire actors
enemies = []

music.play('bg-music')

# Creates a fire actor, places it at a random x, sets direction and adds to enemies list
fire_1 = Actor('fire', (random.randint(0, WIDTH), 300))
fire_1.direction = (0, FIRE_SPEED)
enemies.append(fire_1)

counter = 0
score = 0

def update():
    global counter, score, game_state

    # Check if the game is in the PLAYING state
    if game_state == 'PLAYING':
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
        
        # Check if the heath actor has collided with the coin actor to re-position the coin and increase the score
        if heath.colliderect(coin):
            score += 1
            coin.x, coin.y = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

        # Code to stop Heath going off the screen    
        if heath.left < 0:
            heath.left = 0
        elif heath.right > WIDTH:
            heath.right = WIDTH

        if heath.top < 0:
            heath.top = 0
        elif heath.bottom > HEIGHT:
            heath.bottom = HEIGHT
        
        # Make the enemies move
        for enemy in enemies:
            x_move = enemy.direction[0]
            y_move = enemy.direction[1]
            enemy.x += x_move
            enemy.y += y_move
            
            # If the enemy is moving off the screen, turn it around
            if enemy.x > WIDTH or enemy.x < 0:
                enemy.direction = (- enemy.direction[0], enemy.direction[1])
                
            if enemy.y > HEIGHT or enemy.y < 0:
                enemy.direction = (enemy.direction[0], - enemy.direction[1])
            
            # TODO: Check if the heath actor has collided with an enemy
            if heath.colliderect(enemy):
                game_state = 'GAME_OVER'
    
    # Check if the game is in the GAME_OVER state
    elif game_state == 'GAME_OVER':
        # If the space key is pressed, reset the game
        if keyboard.space:
            reset_game()

            
    counter += 1
    # Check the counter to see if we should create a new enemy
    if counter > NEW_FIRE_AFTER:
        # Create a new enemy and add it
        new_fire = Actor('fire', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        # Set the direction to be random, going in lots of different possible directions.
        new_fire.direction = random.choice([(0, FIRE_SPEED), (0, -FIRE_SPEED), (FIRE_SPEED, 0), (-FIRE_SPEED, 0), (FIRE_SPEED, FIRE_SPEED)])
        enemies.append(new_fire)
        counter = 0
        

def draw():
    # Set the background color before drawing the actors
    screen.fill(BGCOLOUR)

    if game_state == 'PLAYING':
        heath.draw()
        coin.draw()
        for enemy in enemies:
            enemy.draw()
    elif game_state == 'GAME_OVER':
        screen.draw.text('GAME OVER', (400, 300), color='black')
        screen.draw.text('Press SPACE to play again', (400, 350), color='black')
    
    # Draw the score
    screen.draw.text('Score: ' + str(score), (10, 10), color='black')

def reset_game():
    global score, counter, enemies, game_state
    score = 0
    counter = 0
    enemies = []
    game_state = 'PLAYING'

    heath.x, heath.y = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    coin.x, coin.y = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    fire_1.x, fire_1.y = (random.randint(0, WIDTH), 300)
    fire_1.direction = (0, FIRE_SPEED)
    enemies.append(fire_1)


pgzrun.go()
