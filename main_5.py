# imports
#==========

import arcade
import arcade.gui
from arcade import Section

from typing import Optional
from math import sqrt


import imgui
from arcade_imgui import ArcadeRenderer
import arcade_imgui


from typing import List
import random
import string  


# CST
#===========
MAP_TOP_BORDER = 599
MAP_BOT_BORDER = 300

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

DEFAULT_FONT_SIZE = 10
DEFAULT_LINE_HEIGHT = DEFAULT_FONT_SIZE * 3
SECURITY_NO_OVERLAP_BORDER = DEFAULT_LINE_HEIGHT * 2

# LINKS =======================================================

# https://api.arcade.academy/en/latest/examples/sections_demo_3.html#sections-demo-3
# https://api.arcade.academy/en/development/programming_guide/sections.html

# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=arcade.gui.UITextureButton#arcade.gui.UITextureButton

# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=arcade.gui.UITextureButton#arcade.gui.UIAnchorWidget

# https://api.arcade.academy/en/latest/examples/gui_flat_button.html#gui-flat-button
#===================================================================
#button.section,button.name,self.IconSection_interface_status


def emit_click(section, btn_name, interf_status):
    print(f" section {section}  btn {btn_name} has been clicked with interf_status {interf_status}")


# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()
#_______________________________________________________________________________________________

class Infostorage():

    def __init__(self):
        self.name_of_table_imgui: str = ""
        self.list_col_names = [str]
        self.list_of_rows: List[List[str]]

    def test_setup(self):
        self.name_of_table_imgui = "title of the tab from class Infostorage"
        self.list_col_names = ["ID", "File", "Size", "Last modified"]
        self.list_of_rows_OLD = [['FileA.txt','99957 Kb', '12th Feb, 2016 12:19:01'],['ImageQ.png', '349 Kb', '1st Mar, 2016 06:38:22']]
        self.list_of_rows = [['0','FileA.txt','99957 Kb', '12th Feb'],['1','ImageQ.png', '349 Kb', '1st Mar']]





    def randomizer_mini_int(self):
        mini_int = random.randint(3, 9)
        print("called  randomizer_mini_int()")
        return mini_int


    def randomizer_big_int(self):
        big_int = random.randint(50, 9999)
        print("called  randomizer_big_int()")
        return big_int


    def get_random_string_low(self, length):
    #def get_random_string_low(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("called  get_random_string_low()")
        return result_str


    def get_random_string_up(self, length):
    #def get_random_string_up(self):
        letters = string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("called  get_random_string_up()")
        return result_str

        




    def fillupjam(self):

        current_ID = len(self.list_of_rows)

        first = str(current_ID)

        mini_int = self.randomizer_mini_int()
        second= self.randomizer_big_int()
        second= str(second)

        third= self.get_random_string_low(mini_int)

        fourth= self.get_random_string_up(mini_int)



        #jamrow = ['6564646', 'shfsgjjdsfh', 'XYZWH']
        jamrow = [first, second, third, fourth]

        self.list_of_rows.append(jamrow)

    def largerjam(self):

        jamcol = "A_B_C"
        self.list_col_names.append(jamcol)



myInfostorage = Infostorage()
myInfostorage.test_setup()

#________________________________________________________________________________________________

class Datasec(Section):
    """ This represents the place where the game takes place """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        #self.manager = arcade.gui.UIManager() ???
        #self.manager.enable()

        #arcade.set_background_color(arcade.csscolor.DIM_GRAY)
        #arcade.set_background_color(arcade.csscolor.PINK)

        print("\n   Datasec instanciated  \n")


    def on_draw_topi(self, name_of_table_imgui: str):
        imgui.new_frame()
        imgui.begin(name_of_table_imgui)

    def on_draw_cols(self, list_col_names: str):
        len_list_col_names = len(list_col_names)
        col_style = 'fileLlist'
        imgui.columns(len_list_col_names, col_style)


        imgui.separator()

        i=0
        #for colname in list_col_names:
        for i in range(0, len_list_col_names):
            current_col_txt = list_col_names[i]

            imgui.text(current_col_txt)
            imgui.next_column()
        imgui.separator()


    def on_draw_rows_OLD(self, list_of_rows: str):

        imgui.set_column_offset(1, 40)
        imgui.next_column()

        for row in list_of_rows:
            for cell in row:

                imgui.text(cell)
                imgui.next_column()



                
            imgui.next_column()
        
        imgui.columns(1)
        imgui.end()


    def on_draw_rows(self, list_of_rows: str):

        #imgui.set_column_offset(1, 40)
        #imgui.next_column()

        for row in list_of_rows:
            for cell in row:

                imgui.text(cell)
                imgui.next_column()



                
            #imgui.next_column()
        
        imgui.columns(1)
        imgui.end()



    #def on_draw(self, name_of_table_imgui: str, list_col_names: [str], list_of_rows: [[str]]):
    def on_draw(self):



        #name_of_table_imgui = "title of the tab"
        #self.on_draw_topi(name_of_table_imgui)


        #list_col_names = ["ID", "File", "Size", "Last modified"]
        #self.on_draw_cols(list_col_names)


        #list_of_rows = [['FileA.txt','57 Kb', '12th Feb, 2016 12:19:01'],['ImageQ.png', '349 Kb', '1st Mar, 2016 06:38:22']]
        #self.on_draw_rows(list_of_rows)


        #name_of_table_imgui = "title of the tab"
        self.on_draw_topi(myInfostorage.name_of_table_imgui)


        #list_col_names = ["ID", "File", "Size", "Last modified"]
        self.on_draw_cols(myInfostorage.list_col_names)


        #list_of_rows = [['FileA.txt','57 Kb', '12th Feb, 2016 12:19:01'],['ImageQ.png', '349 Kb', '1st Mar, 2016 06:38:22']]
        self.on_draw_rows(myInfostorage.list_of_rows)


        





        imgui.render()

#________________________________________________________________________________________________

class IconSection(Section):

    


    def __init__(self, left: int, bottom: int, width: int, height: int,
             **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)


        self.IconSection_interface_status = "Quiet"

        self.btn_list = []

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.ALMOND)


        self.h_box = arcade.gui.UIBoxLayout(x=0, y=0, vertical=False)

        #-------+++++------------------------------$$$

        self.fn_names = ["add_row", "add_column", "subset_rows", "subset_cols", "look_db", "cell", "bar", "pie", "ascdes", "var"]

        self.fn_icon_3_names = dict()

        for fn_name in self.fn_names:
            name_idle = fn_name + "_idle.png"
            name_hovered = fn_name + "_hovered.png"
            name_pressed = fn_name + "_pressed.png"

            self.fn_icon_3_names[fn_name] = tuple((name_idle, name_hovered, name_pressed))

            button = arcade.gui.UITextureButton(x=100, y=50, 
                texture=arcade.load_texture(f"./icons/{name_idle}"),
                texture_hovered=arcade.load_texture(f"./icons/{name_hovered}"),
                texture_pressed=arcade.load_texture(f"./icons/{name_pressed}"))

            button.name = fn_name
            button.section = "IconSection"

            idx = len(self.btn_list)

            button.idx = idx


            self.btn_list.append(button)



        #.............   

   

            button.on_click = emit_click(button.section,button.name,self.IconSection_interface_status)

            


            self.h_box.add(button.with_space_around(bottom=50))


        #.............   




        
        #____________________________________________________________

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        #start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
        #@settings_button.event("on_click")
        #def on_click_settings(event):
        #    print("Settings:", event)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                #anchor_x="center_x",
                anchor_x="left",
                #anchor_y="center_y",
                anchor_y="bottom",
                child=self.h_box)
        )


        print("\n   IconSection instanciated  \n")



    def on_draw(self):
        #self.clear()
        self.manager.draw()

#_______________________________________________________________________________________________

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        print("\n   ---  GameView starting instanciation \n")
        self.icon_section = IconSection (0,0,SCREEN_WIDTH, 299)
        #self.map_section = Map(0, 300, SCREEN_WIDTH, 299)
        self.data_section = Datasec(0, 600, SCREEN_WIDTH, 299)

        # add the sections
        self.section_manager.add_section(self.icon_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.icon_section)   ")

        #self.section_manager.add_section(self.map_section)
        #print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.map_section)   ")

        self.section_manager.add_section(self.data_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.data_section)   ")

        print("\n   GameView instanciated fully accomplished  ----  \n")



    def on_draw(self):
        arcade.start_render()
        #self.renderer.render(imgui.get_draw_data())  # AttributeError: 'GameView' object has no attribute 'renderer'

#_______________________________________________________________________________________________

class SpecialWindow(arcade.Window):

    def __init__(self):
        
        super().__init__(1900, 960, "init SpecialWindow Basic Example", resizable=True)

        imgui.create_context()
        self.renderer = ArcadeRenderer(self)
        print("\n   SpecialWindow instanciated  \n")


    def on_draw(self):
        #self.clear()
        #imgui.render()
        
        self.renderer.render(imgui.get_draw_data())   #UNCOMMENT WHEN IMGUI PRESENT # self.renderer = impl notebook , que du rose si comment
        #self.clear() #commenter si imgui present

        #arcade.finish_render()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            arcade.exit()

def give_me_a_special_window():
    special_window = SpecialWindow()

    return special_window

#________________________________________________________________________________________________________________

def main():
    
    window = give_me_a_special_window()
    window.clear()
    game = GameView()
    window.show_view(game)
    window.run()

if __name__ == '__main__':
    main()

