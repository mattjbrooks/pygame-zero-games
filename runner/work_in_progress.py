import pgzrun # If using Thonny in Pygame Zero Mode this line is unneeded

player = Actor("player")
player.x = 400 # How many pixels to the right player will appear
player.y = 500 # How many pixels down player will appear
player.jump = 30

cloud = Actor("cloud")
cloud.pos = 1000, 100 # this is the same as setting cloud.x = 1000 and cloud.y = 100

fence = Actor("fence")
fence.pos = 1000, 500

grass = Actor("grass")
grass.pos = 800, 525

music.play("retrobeat")

def draw():
    screen.blit("snow", (0, 0)) # draw the background to the screen (top-left corner at 0, 0) 
    cloud.draw()
    grass.draw()
    fence.draw()
    player.draw()

def update():
    if keyboard.left:
        player.x = player.x - 5 # a shorter way of writing this if you prefer is
                                # player.x -= 5
    elif keyboard.right:
        player.x = player.x + 5 # a shorter way of writing this if you prefer is
                                # player.x += 5
    if keyboard.space: # not elif as we may want to move left or right and jump at same time
        jump()
    move_cloud()
    move_fence()
    move_grass()
    game_gravity()

def jump():
    # We're jumping!
    # Remember at the start we set player.jump to 30
    if player.jump == 30:
        sounds.jump.play()
    player.y = player.y - player.jump
    # Now we will make player.jump smaller
    # so the jump won't go on forever if you hold down space.
    if player.jump > 0:
        player.jump = player.jump - 1

def move_cloud():
    cloud.x = cloud.x - 1
    if cloud.x < -200:
        cloud.x = 1000

def move_fence():
    fence.x = fence.x - 10
    if fence.x < -200:
        fence.x = 1000

def move_grass():   
    grass.x = grass.x - 5
    if grass.x < -100:
        grass.x = 800

def game_gravity():
    if player.y < 500: # if player is in the air
        player.y = player.y + 10 # move them down 10 pixels
    else:
        player.y = 500 # if player isn't in the air put them on the ground
        player.jump = 30 # now we're on the ground we can jump again at full power!

pgzrun.go() # If using Thonny in Pygame Zero Mode this line is unneeded
