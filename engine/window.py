import pygame


# static variables
ORIGINAL_WIDTH, ORIGINAL_HEIGHT = 0, 0
PREV_WIDTH, PREV_HEIGHT, PREV_FLAGS, PREV_DEPTH, PREV_VSYNC = 0, 0, 0, 0, 0

INITIALIZED = False
FRAMEBUFFER = None
INSTANCE = None
WIDTH, HEIGHT = 0, 0
FLAGS = 0
DEPTH = 0
VSYNC = 0

INSTANCE_CHANGED = True
GLOBAL_CLOCK = None

# framebuffer scale and stuff
XSCALE, YSCALE = 1, 1


# static file
def create_instance(t, w, h, f=0, b=32, v=1, framebuffer=False):
    """Only one window instance is available at a time"""
    global INITIALIZED, WIDTH, HEIGHT, FLAGS, DEPTH, VSYNC, INSTANCE, ORIGINAL_HEIGHT, ORIGINAL_WIDTH, FRAMEBUFFER
    if not INITIALIZED:
        ORIGINAL_WIDTH, ORIGINAL_HEIGHT = w, h
        pygame.init()
        INITIALIZED = True
        INSTANCE = pygame.display.set_mode((w, h), flags=f, depth=b, vsync=v)
        if framebuffer:
            FRAMEBUFFER = pygame.Surface((w, h)).convert()
        pygame.display.set_caption(t)
    else:
        INSTANCE = pygame.display.set_mode((w, h), flags=f, depth=b, vsync=v)
        pygame.display.set_caption(t)
    WIDTH, HEIGHT, FLAGS, DEPTH, VSYNC = w, h, f, b, v
    return INSTANCE


def set_title(title):
    """Set window title"""
    pygame.display.set_caption(title)


def set_icon(icon):
    """Set window icon"""
    pygame.display.set_icon(icon)


def get_instance():
    """returns the instance"""
    return INSTANCE


def change_framebuffer(w:int, h:int, f:int):
    """change a framebuffer"""
    global FRAMEBUFFER
    FRAMEBUFFER = pygame.Surface((w, h), flags=f)


def get_framebuffer():
    """returns the framebuffer"""
    return FRAMEBUFFER


def handle_resize(resize_event):
    """Handle window resize event"""
    global PREV_WIDTH, PREV_HEIGHT, WIDTH, HEIGHT
    PREV_WIDTH, PREV_HEIGHT = WIDTH, HEIGHT
    WIDTH, HEIGHT = resize_event.x, resize_event.y


def create_clock(FPS):
    """Creates a pygame clock object"""
    global GLOBAL_CLOCK
    GLOBAL_CLOCK = pygame.time.Clock()


def fill_buffer(color):
    """fill instance framebuffer"""
    global INSTANCE_CHANGED
    FRAMEBUFFER.fill(color)
    INSTANCE_CHANGED = True


def push_buffer(offset):
    """push teh framebuffer onto the window"""
    INSTANCE.blit(FRAMEBUFFER, offset)

def draw(surface, pos):
    """if window was changed"""
    global INSTANCE_CHANGED
    FRAMEBUFFER.blit(surface, pos)
    INSTANCE_CHANGED = True
