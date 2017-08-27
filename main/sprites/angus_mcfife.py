import sys, pygame

class AngusMcFife(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        """ X and Y location on screen """
        self.x = pos[0]
        self.y = pos[1]

        """ image buffers for movement """
        self.up_counter = 0
        self.up = [
            "sprites/assests/0.png",
            "sprites/assests/1.png",
            "sprites/assests/2.png",
            "sprites/assests/3.png",
            "sprites/assests/4.png",
            "sprites/assests/5.png",
            "sprites/assests/6.png",
            "sprites/assests/7.png",
            "sprites/assests/8.png"
        ]

        self.down_counter = 0
        self.down = [
            "sprites/assests/18.png",
            "sprites/assests/19.png",
            "sprites/assests/20.png",
            "sprites/assests/21.png",
            "sprites/assests/22.png",
            "sprites/assests/23.png",
            "sprites/assests/24.png",
            "sprites/assests/25.png",
            "sprites/assests/26.png"
        ]

        self.left_counter = 0
        self.left = [
            "sprites/assests/9.png",
            "sprites/assests/10.png",
            "sprites/assests/11.png",
            "sprites/assests/12.png",
            "sprites/assests/13.png",
            "sprites/assests/14.png",
            "sprites/assests/15.png",
            "sprites/assests/16.png",
            "sprites/assests/17.png"
        ]

        self.right_counter = 0
        self.right = [
            "sprites/assests/27.png",
            "sprites/assests/28.png",
            "sprites/assests/29.png",
            "sprites/assests/30.png",
            "sprites/assests/31.png",
            "sprites/assests/32.png",
            "sprites/assests/33.png",
            "sprites/assests/34.png",
            "sprites/assests/35.png",
        ]

        """ pygame stuff """
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.image = pygame.image.load("sprites/assests/23.png")

    def handle_keys(self):
        """Handle user input"""
        key = pygame.key.get_pressed()
        dist = 1

        # Up
        if key[pygame.K_w]:
            self.y -= dist
            self.image = pygame.image.load(self.up[self.up_counter])
            self.up_counter = (self.up_counter + 1)% len(self.up)

        # Down
        elif key[pygame.K_s]:
            self.y += dist
            self.image = pygame.image.load(self.down[self.down_counter])
            self.down_counter = (self.down_counter + 1)% len(self.down)

        # Left
        if key[pygame.K_a]:
            self.x -= dist
            self.image = pygame.image.load(self.left[self.left_counter])
            self.left_counter = (self.left_counter + 1)% len(self.left)

        # Right
        elif key[pygame.K_d]:
            self.x += dist
            self.image = pygame.image.load(self.right[self.right_counter])
            self.right_counter = (self.right_counter + 1)% len(self.right)

    def update(self):
        self.handle_keys()
        self.rect = pygame.Rect(self.x, self.y, 16, 16)