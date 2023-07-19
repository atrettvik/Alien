# MODULES
import pygame
import os
import random
import time
pygame.font.init()


# PYGAME SETTINGS
WIDTH, HEIGHT = 1280, 840
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien")


# LOAD IMAGES
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# PLAYER SHIP IMAGE
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# LASER IMAGE
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# BACKGROUND
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))



# SHIP FUNCTIONS
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))               
            
            

# GAME FUNCTIONS

def main():
    run = True
    fps = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 40)
    player_vel = 5
    ship = Ship(450, 700)    
    
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        # DRAW TEXT
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        
        ship.draw(WIN)
        
        pygame.display.update()
        
# EVENT LOOP   
    while run:
        clock.tick(fps)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #LEFT
            ship.x -= player_vel
        if keys[pygame.K_d]: #RIGHT
            ship.x += player_vel
        if keys[pygame.K_w]: #UP
            ship.y -= player_vel
        if keys[pygame.K_s]: #DOWN
            ship.y += player_vel

main()