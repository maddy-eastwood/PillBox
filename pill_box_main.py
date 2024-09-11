from pill_box_classes import *
import time

# added to git repo

def main():

    #set size of playing screen
    width = 1000
    height = 700

    #initialize the GUI
    pygame.init()
    pygame.display.set_caption("Pillbox")
    screen = pygame.display.set_mode((width, height))
    start_screen_mode = True

    start_buttons = Buttons(screen)
    start_buttons.add_button(
        event='start',
        width=int(0.09 * width),
        height=int(0.08 * height),
        x=int(width / 2),
        y=int(height / 2),
        font_size=int(0.05 * height),
        label='START')


    # create a playing field variable
    field = None
    selected_event: str = ''
    event_label:str = ''
    input_box_value: int = 0
    bullets_fired = False

    while True:

        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_screen_mode: #welcome screen
                screen.fill('cadetblue1')
                welcome_font = pygame.font.Font(None, int(0.1*height))
                welcome_surf = welcome_font.render("Welcome to Pillbox", True, 'dark blue')
                welcome_rect = welcome_surf.get_rect(center=(int(width/2), int(height/3)))
                screen.blit(welcome_surf, welcome_rect)
                start_buttons.draw_buttons()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    start_events = start_buttons.check_buttons(x, y)
                    if 'start' in start_events:
                        start_screen_mode = False
                        field = Playingfield(height, width, screen)
                        field.draw()

            else:  # in game screen
                # this section handles what to do once a button has been pressed
                # if a button has been pressed, its 'event' label will be in the field_events list
                # selected_event refers to the current button that is selected
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    field_events = field.buttons.check_buttons(x, y)
                    if 'quit' in field_events:
                        pygame.quit()
                        sys.exit()
                    elif 'restart' in field_events:
                        selected_event = ''
                        field.reset_game_parameters()
                        field.compute_field()
                        field.update_game_buttons()
                        field.draw()
                    # FIRE1 MODE
                    elif 'fire1' in field_events:
                        if bullets_fired:
                            field.draw()
                            bullets_fired = False
                        if selected_event != '':
                            field.buttons.unselect_button(selected_event)
                            selected_event = ''
                        print(f'FIRE1: speed={field.velocity1}, angle={field.angle1}')
                        seconds = 0
                        bullet = Bullet(screen, field.velocity1, field.angle1, field.x_lbase, field.y_lplane-(3+field.base_height), seconds)
                        bullet.draw_bullet() #draws initial bullet/starting position on base
                        test = Playingfield.NO_INTERSECTION  # to enter the loop
                        while seconds < 50 and test == Playingfield.NO_INTERSECTION: #while bullet has not had an intersection
                            seconds += 0.25
                            start_bullet_x, start_bullet_y = bullet.current_x, bullet.current_y
                            bullet.update_bullet_1(seconds)
                            test = field.check_game_intersections(start_bullet_x, bullet.current_x,
                                                                  start_bullet_y, bullet.current_y)
                            if test == Playingfield.NO_INTERSECTION:
                                bullet.draw_bullet()
                            pygame.display.update()
                            pygame.time.delay(50)
                        # check if right base was hit
                        if test == Playingfield.RIGHT_BASE:
                            field.player1_score += 100
                            field.buttons.button_dict['player1_score']['label'] = f'PLAYER 1 SCORE: {field.player1_score}'
                            field.buttons.draw_button('player1_score')
                            pygame.time.delay(300)
                            selected_event = ''
                            field.compute_field()
                            field.draw()

                        bullets_fired = True

                    # FIRE2 MODE
                    elif 'fire2' in field_events:
                        if bullets_fired:
                            field.draw()
                            bullets_fired = False
                        if selected_event != '':
                            field.buttons.unselect_button(selected_event)
                            selected_event = ''
                        print(f'FIRE2: speed={field.velocity2}, angle={field.angle2}')
                        seconds = 0
                        bullet = Bullet(screen, field.velocity2, field.angle2, field.x_rbase, field.y_rplane-(3+field.base_height), seconds)
                        bullet.draw_bullet()
                        test = Playingfield.NO_INTERSECTION
                        while seconds < 50 and test == Playingfield.NO_INTERSECTION: #while bullet has not had an intersection
                            seconds += 0.25
                            start_bullet_x, start_bullet_y = bullet.current_x, bullet.current_y
                            bullet.update_bullet_2(seconds)
                            test = field.check_game_intersections(start_bullet_x, bullet.current_x,
                                                                  start_bullet_y, bullet.current_y)
                            if test == Playingfield.NO_INTERSECTION:
                                bullet.draw_bullet()
                            pygame.display.update()
                            pygame.time.delay(50)
                        # check if left base was hit
                        if test == Playingfield.LEFT_BASE:
                            field.player2_score += 100
                            field.buttons.button_dict['player2_score']['label'] = f'PLAYER 2 SCORE: {field.player2_score}'
                            field.buttons.draw_button('player2_score')
                            pygame.time.delay(300)
                            selected_event = ''
                            field.compute_field()
                            field.draw()

                        bullets_fired = True

                    # this section sets up new number input for the selected (clicked) input box
                    elif 'angle1' in field_events:
                        # deselect any prior number input selection
                        if selected_event != '' and selected_event != 'angle1':
                            field.buttons.unselect_button(selected_event)
                        # set up to remember new number input selection
                        field.buttons.select_button('angle1')
                        selected_event = 'angle1'
                        input_box_value = field.angle1
                    elif 'angle2' in field_events:
                        if selected_event != '' and selected_event != 'angle2':
                            field.buttons.unselect_button(selected_event)
                        field.buttons.select_button('angle2')
                        selected_event = 'angle2'
                        input_box_value = field.angle2
                    elif 'velocity1' in field_events:
                        if selected_event != '' and selected_event != 'velocity1':
                            field.buttons.unselect_button(selected_event)
                        field.buttons.select_button('velocity1')
                        selected_event = 'velocity1'
                        input_box_value = field.velocity1
                    elif 'velocity2' in field_events:
                        if selected_event != '' and selected_event != 'velocity2':
                            field.buttons.unselect_button(selected_event)
                        field.buttons.select_button('velocity2')
                        selected_event = 'velocity2'
                        input_box_value = field.velocity2

                # this section handles keypress -- not related to mouseclicks.
                # it will update the input number in the box of the selected event
                if event.type == pygame.KEYDOWN:
                    if selected_event in ['angle1', 'angle2', 'velocity1', 'velocity2']:
                        if event.key >= pygame.K_0 and event.key <= pygame.K_9:
                            input_box_value = input_box_value * 10 + event.key - pygame.K_0
                        elif event.key == pygame.K_BACKSPACE:
                            input_box_value = input_box_value // 10

                        if selected_event == 'angle1':
                            field.angle1 = input_box_value
                            event_label = f'ANGLE: {input_box_value}°'
                        elif selected_event == 'angle2':
                            field.angle2 = input_box_value
                            event_label = f'ANGLE: {input_box_value}°'
                        elif selected_event == 'velocity1':
                            field.velocity1 = input_box_value
                            event_label = f'SPEED: {input_box_value}m/s'
                        elif selected_event == 'velocity2':
                            field.velocity2 = input_box_value
                            event_label = f'SPEED: {input_box_value}m/s'

                        field.buttons.button_dict[selected_event]['label'] = event_label
                        field.buttons.draw_button(selected_event)
                        field.buttons.select_button(selected_event)

        pygame.display.update()

if __name__ == "__main__":
    main()