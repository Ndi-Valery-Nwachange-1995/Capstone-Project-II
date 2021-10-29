# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,
                                  screen_height))  # This creates the screen and gives it the width and height
# specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image).

player = pygame.image.load("image.png")

prize = pygame.image.load("prize.jpg")  # creates the prize and gives it the image found in this folder

enemy = pygame.image.load("enemy.png")

monster = pygame.image.load("monster.jpg")  # creates the monster and gives it the image found in this folder

enemy2 = pygame.image.load("enemy2.jpg")  # creates the player1 and gives it the image found in this folder  (here i
# just rename the name of player to enemy2 using the same picture of dropbox)

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within
# screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()

prize_height = prize.get_height()  # Get the width and height of the prize images in order to do boundary detection
prize_width = prize.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

monster_height = monster.get_height()  # Get the width and height of the monster images in order to do boundary
# detection
monster_width = monster.get_width()

enemy2_height = enemy2.get_height()  # Get the width and height of the player1 images in order to do boundary detection
enemy2_width = enemy2.get_width()

# displaying the height and the width of the player

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later.

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemyXPosition = screen_width  # Make the enemy start off screen and at a random Y position.
enemyYPosition = random.randint(0, screen_height - enemy_height)

monsterXPosition = screen_width  # Make the monster start off screen and at a random Y position.
monsterYPosition = random.randint(0, screen_height - monster_height)

enemy2XPosition = screen_width  # Make the enemy2 start off screen and at a random Y position.
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

prizeXPosition = screen_width  # Make the prize start off screen and at a random Y position.
prizeYPosition = random.randint(0, screen_height - prize_height)
# This checks if the up or down key is pressed. Right now they are not so make them equal to the boolean value (True
# or False) of False. Boolean values are True or False values that can be used to test conditions and test states
# that are binary, i.e. either one way or the other.

keyUp = False
keyDown = False
keyLeft = False  # setting the keyleft to False
keyRight = False  # setting the keyright to False
# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to
# represent real time game play.

while 1:  # This is a looping structure that will loop the indented code until you tell it to stop(in the event where
    # you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater
    # than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...)
    # function to see what boolean value types have. You will learn more about while loop structures later.

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition,
                         playerYPosition))  # This draws the player image to the screen at the position specified. I.e.
    # (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))

    screen.blit(monster, (monsterXPosition, monsterYPosition))

    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))

    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.

            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True

            if event.key == pygame.K_DOWN:  # if pygame.K_DOWN is pressed, it return True (1)
                keyDown = True

            if event.key == pygame.K_LEFT:  # pygame.K_LEFT represents a keyboard key constant.
                keyLeft = True

            if event.key == pygame.K_RIGHT:  # if pygame.K_RIGHT is pressed, it return True (1)
                keyRight = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP:  # if pygame.K_UP is not pressed, it return False (0)
                keyUp = False

            if event.key == pygame.K_DOWN:  # if pygame.K_DOWN is not pressed, it return False (0)
                keyDown = False

            if event.key == pygame.K_LEFT:  # if pygame.K_LEFT is not pressed, it return False (0)
                keyLeft = False

            if event.key == pygame.K_RIGHT:  # if pygame.K_RIGHT is not pressed, it return False (0)
                keyRight = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        if playerYPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1

    if keyDown == True:
        if playerYPosition < screen_height - image_height:  # This makes sure that the user does not move the player
            # below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0:  # This makes sure that the user does not move the player above the window.
            playerXPosition -= 1

    if keyRight == True:
        if playerXPosition < screen_width - image_width:  # This makes sure that the user does not move the player
            # below the window.
            playerXPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:

    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemy:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Test collision of the boxes:

    if playerBox.colliderect(enemyBox):
        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(monsterBox):
        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)
    # If the enemy is off the screen the user wins the game:

    if enemyXPosition < 0 - enemy_width:
        # Display wining status to the user:

        print("You win!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    if monsterXPosition < 0 - monster_width:
        # Display wining status to the user:

        print("You win!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    if playerBox.colliderect(enemy2Box):
        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    if enemy2XPosition < 0 - enemy2_width:
        # Display wining status to the user:

        print("You win!")

        # Quite game and exit window:
        pygame.quit()

        exit(0)

    if playerBox.colliderect(prizeBox):  # if prize collide with player a message will display 'you won'
        # Display you won status to the user:

        print("You won!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)
    # Make enemy approach the player.

    enemyXPosition -= 0.15  # setting prizeXPosition to -=0.15

    monsterXPosition -= 0.20  # setting prizeXPosition to -=0.20

    enemy2XPosition -= 0.25  # setting player1XPosition to -=0.25

    prizeXPosition -= 0.30  # setting prizeXPosition to -=0.30
    # ================The game loop logic ends here. =============
