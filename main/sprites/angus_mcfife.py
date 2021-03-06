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

        self.update_rate = 1

        """ pygame stuff """
        self.image = pygame.image.load("sprites/assests/human_base/23.png")

        self.rect = self.image.get_rect() #pygame.Rect(self.x, self.y, 16, 16)

        sprites.add(self)

        self.moveDist = 2

        # Movement patterns
        self.pattern_counter = 0

        self.example_move = ['s', 's', 's', 's', 's', 's', 's', 's', 'd', 'd', 'd', 'd', 'd', 'd', 'd']


    def move_pattern(self, pattern):
        self.move_sprite(pattern[self.pattern_counter])
        self.pattern_counter = (self.pattern_counter + 1)% len(pattern)

    def move_sprite(self, direction):
        # Up
        if direction == 'w':
            self.upMove()
        elif direction == 's':
            self.downMove()
        elif direction == 'a':
            self.leftMove()
        elif direction == 'd':
            self.rightMove()


    def handle_keys(self):
        """Handle user input"""
        key = pygame.key.get_pressed()

        # Attacks will always take priority
        # + You can also move while attacking... All in one loop cause I am scrub.
        if key[pygame.K_SPACE] or self.status == "attacking":
            self.status = "attacking"

            # Up Attack
            if self.dir == 0:
                self.upAttack()

            # Left Attack
            elif self.dir == 1:
                self.leftAttack()

            # Down Attack
            elif self.dir == 2:
                self.downAttack()

            # Right Attack
            elif self.dir == 3:
                self.rightAttack()

        # Up
        elif key[pygame.K_w]:
            self.upMove()
        # Down
        elif key[pygame.K_s]:
            self.downMove()
        # Left
        elif key[pygame.K_a]:
            self.leftMove()
        # Right
        elif key[pygame.K_d]:
            self.rightMove()

    # Up move
    def upMove(self):
        self.y -= self.moveDist
        self.image = pygame.image.load(self.up[self.up_counter])
        self.up_counter = (self.up_counter + 1)% len(self.up)
        self.dir = 0

    # Down move
    def downMove(self):
        self.y += self.moveDist
        self.image = pygame.image.load(self.down[self.down_counter])
        self.down_counter = (self.down_counter + 1)% len(self.down)
        self.dir = 2

    # Left move
    def leftMove(self):
        self.x -= self.moveDist
        self.image = pygame.image.load(self.left[self.left_counter])
        self.left_counter = (self.left_counter + 1)% len(self.left)
        self.dir = 1

    # Right move
    def rightMove(self):
        self.x += self.moveDist
        self.image = pygame.image.load(self.right[self.right_counter])
        self.right_counter = (self.right_counter + 1)% len(self.right)
        self.dir = 3

    # Up Attack
    def upAttack(self):
        pygame.draw.rect(self.screen, (0,0,255), (self.x, self.y - 10, self.rect.width, 15))
        if self.attack_counter == 5:
            self.up_counter = 0
            self.image = pygame.image.load(self.up[self.up_counter])
            self.attack_counter = 0
            self.status = "moving"
        else:
            if self.buffer_rate == self.update_rate:
                self.image = pygame.image.load(self.up_dagger[self.attack_counter])
                self.attack_counter = (self.attack_counter + 1)% len(self.up_dagger)
                # reset image reset rate.
                self.buffer_rate = 0
            elif self.buffer_rate > 2:
                self.buffer_rate = 0
            else:
                self.buffer_rate += 1

    # Left Attack
    def leftAttack(self):
        pygame.draw.rect(self.screen, (0,0,255), (self.x - 10, self.y, 15, self.rect.width))
        if self.attack_counter == 5:
            self.left_counter = 0
            self.image = pygame.image.load(self.left[self.left_counter])
            self.attack_counter = 0
            self.status = "moving"
        else:
            if self.buffer_rate == self.update_rate:
                self.image = pygame.image.load(self.left_dagger[self.attack_counter])
                self.attack_counter = (self.attack_counter + 1)% len(self.left_dagger)
                # reset image reset rate.
                self.buffer_rate = 0
            elif self.buffer_rate > 2:
                self.buffer_rate = 0
            else:
                self.buffer_rate += 1

    # Down attack
    def downAttack(self):
        pygame.draw.rect(self.screen, (0,0,255), (self.x, self.y + self.rect.height - 10, self.rect.width, 15))
        if self.attack_counter == 5:
            self.down_counter = 0
            self.image = pygame.image.load(self.down[self.down_counter])
            self.attack_counter = 0
            self.status = "moving"
        else:
            if self.buffer_rate == self.update_rate:
                self.image = pygame.image.load(self.down_dagger[self.attack_counter])
                self.attack_counter = (self.attack_counter + 1)% len(self.down_dagger)
                # reset image reset rate.
                self.buffer_rate = 0
            elif self.buffer_rate > 2:
                self.buffer_rate = 0
            else:
                self.buffer_rate += 1

    # Right attack
    def rightAttack(self):
        pygame.draw.rect(self.screen, (0,0,255), (self.x + self.rect.width - 10, self.y, 15, self.rect.width))
        if self.attack_counter == 5:
            self.down_counter = 0
            self.image = pygame.image.load(self.right[self.right_counter])
            self.attack_counter = 0
            self.status = "moving"
        else:
            if self.buffer_rate == self.update_rate:
                self.image = pygame.image.load(self.right_dagger[self.attack_counter])
                self.attack_counter = (self.attack_counter + 1)% len(self.right_dagger)
                # reset image reset rate.
                self.buffer_rate = 0
            elif self.buffer_rate > 2:
                self.buffer_rate = 0
            else:
                self.buffer_rate += 1


    def update(self):


        #self.handle_keys()
        self.move_pattern(self.example_move)

        self.rect = self.image.get_rect() #pygame.Rect(self.x, self.y, 16, 16)
        self.rect.x = self.x
        self.rect.y = self.y

        pygame.draw.rect(self.screen, (255,255,255),self.rect,0)

        # Update the sprites.
        #self.armor_sprites.update()
        #self.armor_sprites.draw(self.screen)