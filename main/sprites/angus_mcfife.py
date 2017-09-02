import sys, pygame

class AngusMcFife(pygame.sprite.Sprite):

    def __init__(self, pos, sprites, screen):
        super().__init__()

        # pygmae display
        self.screen = screen

        # Set the armor type for the character
        self.armor_type = 0


        """ X and Y location on screen """
        self.x = pos[0]
        self.y = pos[1]

        """ image buffers for movement """
        self.up_counter = 0
        self.up = [
            "sprites/assests/human_base/0.png",
            "sprites/assests/human_base/1.png",
            "sprites/assests/human_base/2.png",
            "sprites/assests/human_base/3.png",
            "sprites/assests/human_base/4.png",
            "sprites/assests/human_base/5.png",
            "sprites/assests/human_base/6.png",
            "sprites/assests/human_base/7.png",
            "sprites/assests/human_base/8.png"
        ]

        self.down_counter = 0
        self.down = [
            "sprites/assests/human_base/18.png",
            "sprites/assests/human_base/19.png",
            "sprites/assests/human_base/20.png",
            "sprites/assests/human_base/21.png",
            "sprites/assests/human_base/22.png",
            "sprites/assests/human_base/23.png",
            "sprites/assests/human_base/24.png",
            "sprites/assests/human_base/25.png",
            "sprites/assests/human_base/26.png"
        ]

        self.left_counter = 0
        self.left = [
            "sprites/assests/human_base/9.png",
            "sprites/assests/human_base/10.png",
            "sprites/assests/human_base/11.png",
            "sprites/assests/human_base/12.png",
            "sprites/assests/human_base/13.png",
            "sprites/assests/human_base/14.png",
            "sprites/assests/human_base/15.png",
            "sprites/assests/human_base/16.png",
            "sprites/assests/human_base/17.png"
        ]

        self.right_counter = 0
        self.right = [
            "sprites/assests/human_base/27.png",
            "sprites/assests/human_base/28.png",
            "sprites/assests/human_base/29.png",
            "sprites/assests/human_base/30.png",
            "sprites/assests/human_base/31.png",
            "sprites/assests/human_base/32.png",
            "sprites/assests/human_base/33.png",
            "sprites/assests/human_base/34.png",
            "sprites/assests/human_base/35.png"
        ]

        # Direction of the sprite:
        #   0 = up
        #   1 = left
        #   2 = down
        #   3 = right
        # For now start right.. Why? Because..
        self.dir = 2
        self.attack_counter = 0
        self.up_dagger = [
            "sprites/assests/human_base_dagger/0.png",
            "sprites/assests/human_base_dagger/1.png",
            "sprites/assests/human_base_dagger/2.png",
            "sprites/assests/human_base_dagger/3.png",
            "sprites/assests/human_base_dagger/4.png",
            "sprites/assests/human_base_dagger/5.png"
        ]

        self.left_dagger = [
            "sprites/assests/human_base_dagger/6.png",
            "sprites/assests/human_base_dagger/7.png",
            "sprites/assests/human_base_dagger/8.png",
            "sprites/assests/human_base_dagger/9.png",
            "sprites/assests/human_base_dagger/10.png",
            "sprites/assests/human_base_dagger/11.png"
        ]

        self.down_dagger = [
            "sprites/assests/human_base_dagger/12.png",
            "sprites/assests/human_base_dagger/13.png",
            "sprites/assests/human_base_dagger/14.png",
            "sprites/assests/human_base_dagger/15.png",
            "sprites/assests/human_base_dagger/16.png",
            "sprites/assests/human_base_dagger/17.png"
        ]


        self.right_dagger = [
            "sprites/assests/human_base_dagger/18.png",
            "sprites/assests/human_base_dagger/19.png",
            "sprites/assests/human_base_dagger/20.png",
            "sprites/assests/human_base_dagger/21.png",
            "sprites/assests/human_base_dagger/22.png",
            "sprites/assests/human_base_dagger/23.png"
        ]

        self.status = "moving"

        self.buffer_rate = 0

        """ pygame stuff """
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.image = pygame.image.load("sprites/assests/human_base/23.png")

        sprites.add(self)



    def handle_keys(self):
        """Handle user input"""
        key = pygame.key.get_pressed()
        dist = 2

        # Attacks will always take priority
        # + You can also move while attacking... All in one loop cause I am scrub.
        if key[pygame.K_SPACE] or self.status == "attacking":
            self.status = "attacking"

            # Up Attack
            if self.dir == 0:
                if self.attack_counter == 5:
                    self.up_counter = 0
                    self.image = pygame.image.load(self.up[self.up_counter])
                    self.attack_counter = 0
                    self.status = "moving"
                else:
                    if self.buffer_rate == 2:
                        self.image = pygame.image.load(self.up_dagger[self.attack_counter])
                        self.attack_counter = (self.attack_counter + 1)% len(self.up_dagger)
                        # reset image reset rate.
                        self.buffer_rate = 0
                    elif self.buffer_rate > 2:
                        self.buffer_rate = 0
                    else:
                        self.buffer_rate += 1
            elif self.dir == 1:
                if self.attack_counter == 5:
                    self.left_counter = 0
                    self.image = pygame.image.load(self.left[self.left_counter])
                    self.attack_counter = 0
                    self.status = "moving"
                else:
                    if self.buffer_rate == 2:
                        self.image = pygame.image.load(self.left_dagger[self.attack_counter])
                        self.attack_counter = (self.attack_counter + 1)% len(self.left_dagger)
                        # reset image reset rate.
                        self.buffer_rate = 0
                    elif self.buffer_rate > 2:
                        self.buffer_rate = 0
                    else:
                        self.buffer_rate += 1
            elif self.dir == 2:
                if self.attack_counter == 5:
                    self.down_counter = 0
                    self.image = pygame.image.load(self.down[self.down_counter])
                    self.attack_counter = 0
                    self.status = "moving"
                else:
                    if self.buffer_rate == 2:
                        self.image = pygame.image.load(self.down_dagger[self.attack_counter])
                        self.attack_counter = (self.attack_counter + 1)% len(self.down_dagger)
                        # reset image reset rate.
                        self.buffer_rate = 0
                    elif self.buffer_rate > 2:
                        self.buffer_rate = 0
                    else:
                        self.buffer_rate += 1

            elif self.dir == 3:
                if self.attack_counter == 5:
                    self.down_counter = 0
                    self.image = pygame.image.load(self.right[self.right_counter])
                    self.attack_counter = 0
                    self.status = "moving"
                else:
                    if self.buffer_rate == 2:
                        self.image = pygame.image.load(self.right_dagger[self.attack_counter])
                        self.attack_counter = (self.attack_counter + 1)% len(self.right_dagger)
                        # reset image reset rate.
                        self.buffer_rate = 0
                    elif self.buffer_rate > 2:
                        self.buffer_rate = 0
                    else:
                        self.buffer_rate += 1



        # Up
        elif key[pygame.K_w]:
            self.y -= dist
            self.image = pygame.image.load(self.up[self.up_counter])
            self.up_counter = (self.up_counter + 1)% len(self.up)
            self.dir = 0

        # Down
        elif key[pygame.K_s]:
            self.y += dist
            self.image = pygame.image.load(self.down[self.down_counter])
            self.down_counter = (self.down_counter + 1)% len(self.down)
            self.dir = 2

        # Left
        if key[pygame.K_a]:
            self.x -= dist
            self.image = pygame.image.load(self.left[self.left_counter])
            self.left_counter = (self.left_counter + 1)% len(self.left)
            self.dir = 1

        # Right
        elif key[pygame.K_d]:
            self.x += dist
            self.image = pygame.image.load(self.right[self.right_counter])
            self.right_counter = (self.right_counter + 1)% len(self.right)
            self.dir = 3

    def update(self):
        self.handle_keys()
        self.rect = pygame.Rect(self.x, self.y, 16, 16)

        # Update the sprites.
        #self.armor_sprites.update()
        #self.armor_sprites.draw(self.screen)