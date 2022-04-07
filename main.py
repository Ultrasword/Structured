import pygame

import engine
from engine import window, clock, user_input, handler, draw
from scripts import user_block

background = (255, 255, 255)

# create essential instances
window.create_instance("Structured", 1280, 720, f=pygame.RESIZABLE)
window.change_framebuffer(1280, 720, pygame.SRCALPHA)


# init libraries
# user_block.setup()



HANDLER = handler.Handler()

HANDLER.add_persist_entity(user_block.UserBin((100,100), (300,300)))
# HANDLER.add_persist_entity(user_block.UserBin((500, 100), (400, 200)))


clock.start(fps=30)
window.create_clock(clock.FPS)
running = True
while running:
    # fill instance
    window.get_instance().fill(background)

    # updates
    HANDLER.handle_entities(clock.delta_time)
    # render
    if window.INSTANCE_CHANGED:
        pygame.display.update()
        window.INSTANCE_CHANGED = False

        # update keyboard
    user_input.update()
    # for loop through events
    for e in pygame.event.get():
        # handle different events
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            # keyboard press
            user_input.key_press(e)
        elif e.type == pygame.KEYUP:
            # keyboard release
            user_input.key_release(e)
        elif e.type == pygame.MOUSEMOTION:
            # mouse movement
            user_input.mouse_move_update(e)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # mouse press
            user_input.mouse_button_press(e)
        elif e.type == pygame.MOUSEBUTTONUP:
            # mouse release
            user_input.mouse_button_release(e)
        elif e.type == pygame.WINDOWRESIZED:
            # window resized
            window.handle_resize(e)
            user_input.update_ratio(window.WIDTH, window.HEIGHT, window.ORIGINAL_WIDTH, window.ORIGINAL_HEIGHT)
        elif e.type == pygame.WINDOWMAXIMIZED:
            # window maximized
            window.get_instance().fill(background)
            # re render all entities
            HANDLER.render_all()
            # push frame
            pygame.display.update()
            # prevent re push
            window.INSTANCE_CHANGED = False
        elif e.type == pygame.WINDOWMINIMIZED:
            # window minimized
            clock.FPS = 10
        elif e.type == pygame.WINDOWRESTORED:
            # window restored from minimization
            clock.FPS = 30

    # update clock
    clock.update()
    window.GLOBAL_CLOCK.tick(clock.FPS)

pygame.quit()
