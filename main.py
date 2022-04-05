import pygame

import engine
from engine import window, clock, user_input


background = (255, 255, 255)

# create essential instances
window.create_instance("Structured", 1280, 720, f=pygame.RESIZABLE)
window.change_framebuffer(1280, 720, pygame.SRCALPHA)




clock.start(fps=30)
window.create_clock(clock.FPS)
running = True
while running:
    # updates
    window.FRAMEBUFFER.fill(background)
    

    # render
    window.INSTANCE.blit(window.FRAMEBUFFER, (0,0))
    pygame.display.update()

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

    # print(user_input.get_mouse_pos())

    # update clock
    clock.update()
    window.GLOBAL_CLOCK.tick(clock.FPS)

pygame.quit()
