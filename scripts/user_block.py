from engine import handler, state, filehandler, user_input, draw, window


DEFAULT_THEME_COLOR = (44, 74, 94)
CURVE_BORDER_RADIUS = 10

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

    def render(self):
        """Render the object"""
        if self.transform[0] or self.transform[1]:
            self.dirty = True
            self.pos[0] += self.transform[0]
            self.pos[1] += self.transform[1]
            self.transform[0] = 0
            self.transform[1] = 0
        if self.dirty:
            self.dirty = False
            window.draw(self.sprite, self.pos)

    def change_sprite(self, new):
        """Change the sprite"""
        self.sprite = new
        self.dirty = True

DEFAULT_SOLID_BIN = None


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

        # set to default background
        self.change_sprite(DEFAULT_SOLID_BIN)
    
    def add_child(self, child_id: int):
        """Add a child to the user bin - O(n) time"""
        self.children.append(child_id)
    
    def remove_child(self, child_id: int):
        """Remove a child from the user bin - O(n) time"""
        self.children.remove(child_id)
    
    def update(self, dt):
        """Update the userbin"""
        self.transform[0] += 30 * dt
        pass



def setup():
    global DEFAULT_SOLID_BIN
    DEFAULT_SOLID_BIN = filehandler.make_surface(100, 100, draw.EMPTY_ALPHA)
    draw.DRAW_RECT(DEFAULT_SOLID_BIN, DEFAULT_THEME_COLOR, (0, 0, 100, 100), 0, CURVE_BORDER_RADIUS)


