import pygame
from engine import handler, state, filehandler, user_input, draw, window, core_utils


DEFAULT_THEME_COLOR = (44, 74, 94)

class UserBlock(handler.PersistentObject):
    """
    Persisting User Block object

    an object that the user can drag around and toss into UserBins
    """
    def __init__(self, pos: list, area: list):
        """Constructor for UserBlock"""
        super().__init__()
        # general position
        self.pos = list(pos)
        self.area = list(area)

        # visual aspect
        self.sprite = None
        self.sprite_path = None

        # limit window updating
        self.dirty = True
        self.transform = [0,0]
    
    def update(self, dt):
        """standard update function"""
        pass

    def handle_changes(self):
        """handle changes in transform or rotation, etc"""
        if self.transform[0] or self.transform[1]:
            self.dirty = True
            self.pos[0] += self.transform[0]
            self.pos[1] += self.transform[1]
            self.transform[0] = 0
            self.transform[1] = 0

    def render(self):
        """Render the object"""
        if self.dirty:
            self.dirty = False
            window.draw(self.sprite, self.pos)

    def change_sprite(self, new, size: tuple):
        """Change the sprite"""
        self.sprite = filehandler.scale(new, size)
        self.dirty = True


class UserBin(UserBlock):
    """
    Persistng User Bin object

    is a bin
    - can store UserBlocks within a container
    - render and store them for neat workspace
    """
    def __init__(self, pos: list, area: list):
        """Constructor for UserBin"""
        super().__init__(pos, area)
        # to handle children - children = list of id's
        # we can get the actual child objects from handler
        self.children = []

        # create pygame rect object for easy rendering
        self.rect = core_utils.make_pygame_rect(self.pos[0], self.pos[1], self.area[0], self.area[1])
        self.curve_radius = self.area[0] // 8

    def add_child(self, child_id: int):
        """Add a child to the user bin - O(n) time"""
        self.children.append(child_id)
    
    def remove_child(self, child_id: int):
        """Remove a child from the user bin - O(n) time"""
        self.children.remove(child_id)
    
    def update(self, dt):
        """Update the userbin"""
        if user_input.is_key_pressed(pygame.K_a):
            self.transform[0] -= 50 * dt
        if user_input.is_key_pressed(pygame.K_d):
            self.transform[0] += 50 * dt
        if user_input.is_key_pressed(pygame.K_w):
            self.transform[1] -= 50 * dt
        if user_input.is_key_pressed(pygame.K_s):
            self.transform[1] += 50 * dt
    
    def handle_changes(self):
        """Handle changes made in position"""
        if self.transform[0] or self.transform[1]:
            self.dirty = True
            self.pos[0] += self.transform[0]
            self.pos[1] += self.transform[1]
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]
            self.transform[0] = 0
            self.transform[1] = 0

    def render(self):
        """Render UserBin Object"""
        if self.dirty:
            # we have positional data, area data, and color data
            # draw using pygame built in functions
            # TODO - text renderering
            draw.DRAW_RECT(window.get_instance_for_draw(), DEFAULT_THEME_COLOR, self.rect, 0, self.curve_radius)
            self.dirty = False


