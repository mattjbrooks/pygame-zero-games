import pgzrun
import extra # trinket-only (not needed for Pi version)

player = Actor("player")
player.x = 400 # How many pixels to the right player will appear
player.y = 500 # How many pixels down player will appear
player.jump = 30
player.lives = 3
player.score = 0

cloud = Actor("cloud")
cloud.pos = 1000, 100 # this is the same as setting cloud.x = 1000 and cloud.y = 100

fence = Actor("fence")
fence.pos = 1500, 500

grass = Actor("grass")
grass.pos = 800, 525

coin = Actor("coin")
coin.pos = 40, 30

heart = Actor("heart")
heart.pos = 760, 30

music.play("retrobeat")

def draw():
    screen.blit("snow", (0, 0)) # draw the background to the screen (top-left corner at 0, 0) 
    cloud.draw()
    grass.draw()
    fence.draw()
    coin.draw()
    heart.draw()
    player.draw()
    screen.draw.text(str(player.score), fontsize = 60, color = "orange", topleft = (70, 10))
    screen.draw.text(str(player.lives), fontsize = 60, color = "red", topleft = (700, 10))
    if player.lives == 0:
        screen.draw.text("Game Over", fontsize = 100, color = "orange", center = (400, 300))
    
def update():
    if player.lives > 0:
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
        move_player_down()
        check_for_collision()

def jump():
    # We're jumping!
    player.y = player.y - player.jump
    # Remember at the start we set player.jump to 30
    if player.jump == 30:
        sounds.jump.play()
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
        player.score = player.score + 1

def move_grass():   
    grass.x = grass.x - 5
    if grass.x < -100:
        grass.x = 800

def move_player_down():
    if player.y < 500: # if player is in the air
        player.y = player.y + 10 # move them down 10 pixels
    else:
        player.y = 500 # if player isn't in the air put them on the ground
        player.jump = 30 # now we're on the ground we can jump again at full power!

def check_for_collision():
    # if player has collided with the center of the fence and isn't a ghost
    if player.collidepoint(fence.center) and player.image == "player":
        player.lives = player.lives - 1
        player.image = "ghost" # change player's image to a transparent ghost
        clock.schedule(change_back, 1) # schedule change_back to run 1 second from now

def change_back():
    player.image = "player"

pgzrun.go()
