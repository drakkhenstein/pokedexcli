import pygame
import sys
from constants import *
from player import *
from circleshape import *
from enemy import *
from battlefield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    #asteroids = pygame.sprite.Group()
    #shots = pygame.sprite.Group()
    #bullets = pygame.sprite.Group()

    Enemy.containers = (enemies, updatable, drawable)
    #Asteroid.containers = (asteroids, updatable, drawable)
    #Shot.containers = (shots, updatable, drawable)
    
    Battlefield.containers = updatable
    battlefield = Battlefield()
    #AsteroidField.containers = updatable
    #asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #pause = False

        updatable.update(dt)

        #while pause is False:
            #updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        for enemy in enemies:
            if enemy.collision(player):
                screen.fill("black")
                #pause = True
                #dt = clock.tick(0)  # seconds
                #updatable.update(dt + 1)  # freeze the game
                
                #print("Game Over!")
                #pygame.quit()
                #sys.exit()


        pygame.display.flip()

        dt = clock.tick(60) / 1000  # seconds
    print ("  *** Welcome to Dragon Tactics! ***  ")
    print ("\n")
    print ("  Use the arrow keys to move your dragon around the screen.  ")
    print ("  *** Thank you for playing! ***  ")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()
