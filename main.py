import pygame

import engine
from engine import window, clock, user_input, handler, draw
from scripts import user_block

background = (255, 255, 255)

# create essential instances
window.create_instance("Structured", 1280, 720, f=pygame.RESIZABLE)
window.change_framebuffer(1280, 720, pygame.SRCALPHA)


# init libraries
user_block.setup()



HANDLER = handler.Handler()

HANDLER.add_persist_entity(user_block.UserBin((0,0), (100,100)))


clock.start(fps=30)
window.create_clock(clock.FPS)
running = True
while running:
    # updates
    window.fill_buffer(background)
    HANDLER.handle_entities(clock.delta_time)

    draw.DEBUG_DRAW_LINES(window.FRAMEBUFFER, (255, 0, 0), True, ((100, 100), (300, 100), (300, 300), (100, 300)), 1)
    draw.DRAW_RECT(window.FRAMEBUFFER, user_block.DEFAULT_THEME_COLOR, (100, 100, 300, 300), 0, user_block.CURVE_BORDER_RADIUS)

    # render
    if window.INSTANCE_CHANGED:
        window.push_buffer((0,0))
        pygame.display.flip()

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
            pass
        elif e.type == pygame.WINDOWMINIMIZED:
            clock.FPS = 10
        elif e.type == pygame.WINDOWRESTORED:
            clock.FPS = 30

    # print(user_input.get_mouse_pos())

    # update clock
    clock.update()
    window.GLOBAL_CLOCK.tick(clock.FPS)

pygame.quit()
