from typing import Optional

import arcade

import arcade.gui as gui

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()




class ScreenPart(arcade.Section):
    """
    This represents a part of the View defined by its
    boundaries (left, bottom, etc.)
    """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.selected: bool = False  # if this section is selected

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a text label
        self.label = arcade.gui.UILabel(
            text="look here for change",
            text_color=arcade.color.DARK_RED,
            width=350,
            height=40,
            font_size=24,
            font_name="Kenney Future")

        # Create an text input field
        self.input_field = gui.UIInputText(
          color=arcade.color.DARK_BLUE_GRAY,
          font_size=24,
          width=200,
          text='Hello ..')

        # Create a button
        submit_button = gui.UIFlatButton(
          color=arcade.color.DARK_BLUE_GRAY,
          text='Submit')
        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        submit_button.on_click = self.on_click 
        
        self.v_box = gui.UIBoxLayout()
        self.v_box.add(self.label.with_space_around(bottom=0))
        self.v_box.add(self.input_field)
        self.v_box.add(submit_button)
        self.v_box.add(QuitButton(text="Quit"))



        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
        
        


    def update_text(self):
        print(f"updating the label with input text '{self.input_field.text}'")
        self.label.text = self.input_field.text    

    def on_click(self, event):
        print(f"click-event caught: {event}")
        self.update_text()

        
    def on_draw(self):
        #arcade.start_render()
        

        #self.sprite_list.draw()
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color.RED)
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color.YELLOW)



        self.manager.draw()

        


        
    #def on_update(self, delta_time: float):
        # call on_update on the owned Box
        #self.box.on_update(delta_time)


    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float,
                      _buttons: int, _modifiers: int):
        # if we hold a box, then whe move it at the same rate the mouse moves
        #if self.hold_box:
        #    self.hold_box.position = x, y
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # if we pick a Box with the mouse, "hold" it and stop its movement
        #if self.box.collides_with_point((x, y)):
        #    self.hold_box = self.box
        #    self.hold_box.stop()
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        # if hold_box is True because we pick it with on_mouse_press
        # then release the Box
        #if self.hold_box:
        #    self.hold_box.release()
        pass

    def on_mouse_enter(self, x: float, y: float):
        # select this section
        self.selected = True

    def on_mouse_leave(self, x: float, y: float):
        # unselect this section
        self.selected = False

        # if we are holding this section box and we leave the section
        # we release the box as if we release the mouse button
        #if self.hold_box:
        #    self.hold_box.release()


class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # add sections to the view

        # 1) First section holds half of the screen
        self.Left_ScreenPart = ScreenPart(0, 0, self.window.width / 2,
                                    self.window.height, name='Left')

        self.section_manager.add_section(self.Left_ScreenPart)

        # 2) Second section holds the other half of the screen
        #self.Right_ScreenPart = ScreenPart(self.window.width / 2, 0,
        #                            self.window.width / 2, self.window.height,
        #                            name='Right')



        #self.section_manager.add_section(self.Right_ScreenPart)


    def on_draw(self):
        # clear the screen
        self.clear(arcade.color.BEAU_BLUE)

        # draw a line separating each Section
        arcade.draw_line(self.window.width / 2, 0, self.window.width / 2,
                         self.window.height, arcade.color.BLACK, 1)
        #arcade.start_render()

        #for sec in self.section_manager:
        #    sec.draw()


        #self.section_manager.draw()
        #self.Left_ScreenPart.draw()
        self.Left_ScreenPart.on_draw()



def main():
    # create the window
    window = arcade.Window()

    # create the custom View. Sections are initialized inside the GameView init
    view = GameView()

    # show the view
    window.show_view(view)

    # run arcade loop
    window.run()


if __name__ == '__main__':
    main()
