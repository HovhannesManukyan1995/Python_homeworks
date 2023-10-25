#Check import modules
try:
    import os
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'OS' module:Install it")
    exit()
try:
    import sys
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'SYS' module:Install it")
    exit()
try:
    import pygame
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'PYGAME' module:Install it")
    exit()

# Class for the orange dude
class Player():
    
    def __init__(self):
        #Rect mean 
        self.rect = pygame.Rect(22, 22, 16, 16)

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

#Class to hold a wall rect
class Wall():
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame , Pygame to center the game window on the screen
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((640, 352))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
def level_up(cnt):
    if cnt == 0:
        level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W   W                        W         W",
            "W         WWWWWWWWWWWW  WWWW W         W",
            "W   WWWW  W     W    W  W              W",
            "W   W        WWWW    W  W   WWWWW WW WWW",
            "W WWW  WWWW          W  WWWWW     W  E W",
            "W   W     WWW        W      W     W    W",
            "W   W     W   W W    WWWWWWWW     W WW W",
            "W   WWW WWW   W W      W          W WW W",
            "W     W   W   WWWWWWWWWW   WWWWWW W  W W",
            "WWW   W   WWWWW W           WWWW  W  W W",
            "W W      WW           WWWWWWWWWWWWW    W",
            "W WWWWWWWW   WWWWW    W           W   WW",
            "W            W   WWWWWW   WWWWW   WWW  W",
            "W WWWWWWWWWWWW        W   W   W   W    W",
            "W W          W            WWWWW   W  WWW" ,
            "W    WWWWW   W WWWW   W   W       W    W" ,
            "WWWWWW   W   W W      W   W      WWWWW W" ,
            "W        W            W          W     W" ,
            "W        WWWWWWW      WWWWWWWWWWWW     W" ,
            "W                                      W" ,
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    if cnt == 1:
        level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W                                      W",
            "W   WW WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W",
            "WWWWW           W                      W",
            "W   W WWWWWWWWW WWWWWWWWWWWWWWWW WWWWWWW",
            "W WWW   W            W  W W W     W    W",
            "W   W   WWW          W      W     W    W",
            "W   W   W     W W    WWWWWWWW     W    W",
            "W   WWW WWW   W W      W   W      W    W",
            "W     W   W   W WWWWWWWW   WWWWW WW    W",
            "W     W   W   W             W W        W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWW WWWWWWW WWWWW",
            "W         W                W           W",
            "W         W WWWWWWWWWWWWWW W           W" ,
            "W         W W            W W           W" ,
            "W  WWWWW    W  WW     WW W     WWWWW   W",
            "W  W   W  WWW   WW   WW  WWW       W   W",
            "W  WWWWW  W      WWEWW     W   WWWWW   W" ,
            "W  W      W       WWW      W       W   W" ,
            "W  W      W        W       W   WWWWW   W" ,
            "W                                      W" ,
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    if cnt == 2:
            level = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W        WW    W W W W W W W W W W W W W",
            "W  WWW  W    W W                     WWW",
            "W  W E WW WWWW W   W  WWWWWWWWWWW    W W",
            "W  WWWWW  W    W   W  W              WWW",
            "W         W    W   W  W              W W",
            "W   WWWWWWW    W   W  WWWWWW WWWWWWWWWWW",
            "W     W        W   W       W   W W W W W",
            "W     W   W   WWWWWW       W   WWWWWWWWW",
            "W     W   WWWW   W W                   W",
            "WWWWWWW  WW  WWWWW W       W           W",
            "W              W W WWWWWWWWWWWW        W",
            "W      WWWWWW  W W  WW   W    W        W",
            "W      W       WWWWWWWW WWW   W        W" ,
            "WWWWWWWW        W     W       W  WWWWWWW" ,
            "W        WWWWWWWWW   WWWWWWWWWW        W",
            "W      WW   W              W   WW      W",
            "W     W     W  W  WWW  W   W     W     W" ,
            "W   WW         W       W          WW   W" ,
            "W  W        W  W       W   W        W  W" ,
            "W           W     WWW      W           W" ,
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    return level
#Set global variable ` count
cnt = 0
def modify_level_up():
    global cnt 
    cnt += 1
#Set cube W -> Wall E -> Mark
def set_cube(newlevel):
    walls.clear()
    x = y = 0
    for row in newlevel:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0
    return end_rect
#End rect was take for set cube 
def draw_cube(end_rect):
    while True:
        clock.tick(80)
        # This method is commonly used for checking continuous key presses
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)

        #Just added this to make it slightly fun ;)
        if player.rect.colliderect(end_rect):
            return True

        image = pygame.image.load("/home/davit/Desktop/lab.png")
        screen.blit(image, (0, 0)) 
        
        for wall in walls:
            pygame.draw.rect(screen,(241,194,125), wall.rect)

        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
        clock.tick(360)

        
def main():
    while cnt < 3:  # Change this to the number of levels you have
        end_rect = set_cube(level_up(cnt))
        if draw_cube(end_rect):
            modify_level_up()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
