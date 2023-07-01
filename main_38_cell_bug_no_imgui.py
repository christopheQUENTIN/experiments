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

from arcade.gui import UITextureButton

from typing import List
import random
import string  


import numpy as np

import matplotlib.pyplot as plt

# CST
#===========
MAP_TOP_BORDER = 599
MAP_BOT_BORDER = 300

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

DEFAULT_FONT_SIZE = 10
DEFAULT_LINE_HEIGHT = DEFAULT_FONT_SIZE * 3
SECURITY_NO_OVERLAP_BORDER = DEFAULT_LINE_HEIGHT * 2


BTN_WIDTH = 190
BTN_HEIGHT = 140

# LINKS =======================================================

# https://api.arcade.academy/en/latest/examples/sections_demo_3.html#sections-demo-3
# https://api.arcade.academy/en/development/programming_guide/sections.html

# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=arcade.gui.UITextureButton#arcade.gui.UITextureButton

# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=arcade.gui.UITextureButton#arcade.gui.UIAnchorWidget

# https://api.arcade.academy/en/latest/examples/gui_flat_button.html#gui-flat-button



# https://imgui-datascience.readthedocs.io/en/latest/  
# https://snyk.io/advisor/python/imgui/example"

#===================================================================

print("on_click_start  is IMPORTANT   !!!!!!!!!")

print(" \n\n   ++++++++++  https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/")

print(" \n\n   ++++++++++  https://stackoverflow.com/questions/43925337/matplotlib-returning-a-plot-object")
print(" \n\n   ++++++++++  https://stackoverflow.com/questions/14936646/how-to-return-a-matplotlib-figure-figure-object-from-pandas-plot-function")
print(" \n\n   ++++++++++  https://stackoverflow.com/questions/37427362/plt-show-shows-full-graph-but-savefig-is-cropping-the-image")

#_______________________________________________________________________________________________

class Infostorage():

    def __init__(self):
        self.name_of_table_imgui: str = ""
        self.list_col_names = [str]
        self.list_of_rows: List[List[str]]

    def test_setup(self):
        self.name_of_table_imgui = "title of the tab from class Infostorage"
        self.list_col_names = ["ID", "File", "Size", "Last modified", "Lets make a pie !"]
        
        self.list_of_rows = [['0','FileA.txt','99957 Kb', '12th Feb','45'],
        ['1','Wonderfull.txt', '349 Kb', '1st Mar', '30'],
         ['2','Python_and_Rust.txt', '287 Kb', '1st Mar', '20'],
         ['3','Mojo.txt', '149 Kb', '9st Mar', '5']]





    @property
    def len_list_of_rows(self):
        return len(self.list_of_rows)


    def del_ID_1_and_2(self):
        del self.list_of_rows[1:2]
        print(" myInfostorage.del_ID_1_and_2()    just called")



    def del_col_2(self):
        print(" myInfostorage.del_col_2()    just called")
        for row in self.list_of_rows:
            del row[2]

        del myInfostorage.list_col_names[2]


    def reverse_from_index(self):
        self.list_of_rows.reverse()




    @property
    def len_of_cols(self):
        return len(self.list_of_rows[0])



    @property
    def pie_col_index(self):
        return self.list_col_names.index("Lets make a pie !")
        
    


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

        

    def fillupjam_OLD(self):

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


    

    def fillupjam_BEST(self):

        current_ID = self.len_list_of_rows
        first = str(current_ID)
        jamrow = [first]

        #for col in self.len_of_cols:
        for col in range(self.len_of_cols - 1):
            if col != self.pie_col_index -1:
                #newdata = 'new__data'
                newdata = self.get_random_string_low(self.randomizer_mini_int())
                jamrow.append(newdata)
            else:
                #newdata = '13'
                newdata = self.randomizer_mini_int()
                newdata = str(newdata)
                jamrow.append(newdata)


        self.list_of_rows.append(jamrow)

        

    


    def largerjam(self):

        #jamcol = "A_B_C"
        jamcol = self.get_random_string_up(self.randomizer_mini_int())

        self.list_col_names.append(jamcol)

        for row in myInfostorage.list_of_rows:
            row.append(self.get_random_string_low(self.randomizer_mini_int()))



myInfostorage = Infostorage()
myInfostorage.test_setup()

#________________________________________________________________________________________________

class Datasec(Section):
    """ This represents the place where the game takes place """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        
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
        self.on_draw_topi(myInfostorage.name_of_table_imgui)


        #list_col_names = ["ID", "File", "Size", "Last modified"]
        self.on_draw_cols(myInfostorage.list_col_names)


        #list_of_rows = [['FileA.txt','57 Kb', '12th Feb, 2016 12:19:01'],['ImageQ.png', '349 Kb', '1st Mar, 2016 06:38:22']]
        self.on_draw_rows(myInfostorage.list_of_rows)

        







        #..         imgui.core.ImGuiError: ImGui assertion error ((g.FrameCount == 0 || g.FrameCountEnded == g.FrameCount) && "Forgot to call Render() or EndFrame() at the end of the previous frame?")
        imgui.end_frame()

        #..

        imgui.render()


"""
x = 0, y = 0, width = None, height = None, texture = None, texture_hovered = None, texture_pressed = None,
         text = '', scale = None, size_hint =None, size_hint_min =None, size_hint_max =None, style =None,
"""

# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=UITextureButton#arcade.gui.UITextureButton
# super().__init__(x: float = 0, y: float = 0, width: Optional[float] = None, height: Optional[float] = None, texture: Optional[arcade.texture.Texture] = None, texture_hovered: Optional[arcade.texture.Texture] = None, texture_pressed: Optional[arcade.texture.Texture] = None, text: str = '', scale: Optional[float] = None, size_hint=None, size_hint_min=None, size_hint_max=None, style=None, **kwargs)


#def add_row():depuis pie modal => TypeError: add_row() takes 0 positional arguments but 1 was given
def add_row(returned):
    print("fn  add_row  just called")
    #myInfostorage.fillupjam()
    #myInfostorage.fillupjam_OLD()
    myInfostorage.fillupjam_BEST()

    
#def add_column():  depuis pie modal => TypeError: add_column() takes 0 positional arguments but 1 was given  
def add_column(returned):
    print("fn  add_column  just called")
    myInfostorage.largerjam()

#def subset_rows():
def subset_rows(returned):
    print("fn  subset_rows  just called")
    myInfostorage.del_ID_1_and_2()


#def subset_cols():    
def subset_cols(returned):
    print("fn  subset_cols  just called")
    myInfostorage.del_col_2()

def look_db():
    print("fn  look_db  just called")


#def cell():
def cell(returned):
    print("\n\n\n  fn  cell  just called")

    print(">>>>     https://stackoverflow.com/questions/28757389/pandas-loc-vs-iloc-vs-at-vs-iat       ...There are two primary ways...")

    returned['cell_modal_section'].enabled = True

    
    #cellY = input("cellY   : ") #str to print txt but integer to access !
    #cellX = input("cellX   : ")



    #print(f" cellY {cellY}     cellX  {cellX}")
    #print(f" row or ID ? {cellY}     column name  {myInfostorage.list_col_names[int(cellX)]}")
    #print(f"     has cell value  {myInfostorage.list_of_rows[int(cellY)][int(cellX)]}")









# (returned) # il faut descendree dans returned['modal_section']

#def bar():
def bar(returned):
    print("fn  bar  just called")

    print(f"  returned {returned}   type(returned) {type(returned)}      ")
    print("..........................................................................")

    returned['bar_modal_section'].enabled = True




    
def pie(returned):
    print("fn  pie  just called")




    print(f"$$$$$$$$$$$$$$$$$      myInfostorage.pie_col_index   {myInfostorage.pie_col_index}     ")

    #x=1/0

    returned['pie_modal_section'].enabled = True


#def ascdes(): # ascdes() takes 0 positional arguments but 1 was given
def ascdes(returned):
    print("fn  ascdes  just called")

    myInfostorage.reverse_from_index()

    
    

def var():
    print("fn  var  just called")
    #self.view.map_section.add_blue_line()  # NameError: name 'self' is not defined
    #view.map_section.add_blue_line() # NameError: name 'view' is not defined

    #myInfostorage.fillupjam()

    #print(f" .......myInfostorage.list_of_rows = {myInfostorage.list_of_rows}")

    for row in myInfostorage.list_of_rows:
        print(f" \n ... {row}")

    
#________________________________________________________________________________________________

class IconSection(Section):

    def __init__(self, left: int, bottom: int, width: int, height: int,
             **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)


        # return _Rect(x - pl, y - pb, w + pl + pr, h + pb + pt) TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

        #self.left = left
        #self.bottom = bottom
        #self.width = width
        #self.height = height


        self.IconSection_interface_status = "Quiet"
        self.btn_list = []

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.ALMOND)
        self.h_box = arcade.gui.UIBoxLayout(x=0, y=0, vertical=False)

        #-------+++++------------------------------$$$

        self.fn_names = ["add_row", "add_column", "subset_rows", "subset_cols", "look_db", "cell", "bar", "pie", "ascdes", "var"]
        self.name2fn = {"add_row":add_row,"add_column":add_column,"subset_rows":subset_rows,"subset_cols":subset_cols,"look_db":look_db,"cell":cell,"bar":bar,"pie":pie,"ascdes":ascdes, "var":var}


        self.fn_icon_3_names = dict()

        for fn_name in self.fn_names:
            name_idle = fn_name + "_idle.png"
            name_hovered = fn_name + "_hovered.png"
            name_pressed = fn_name + "_pressed.png"

            self.fn_icon_3_names[fn_name] = tuple((name_idle, name_hovered, name_pressed))

            idx = len(self.btn_list)



            button = UITextureButton(x=0, y=0, 
                texture=arcade.load_texture(f"./icons/{name_idle}"),
                texture_hovered=arcade.load_texture(f"./icons/{name_hovered}"),
                texture_pressed=arcade.load_texture(f"./icons/{name_pressed}"))

            #      >>>________________________ monkey patching >>>

            button.name = fn_name
            button.section="icon_section"
            button.idx=idx

            button.on_click = self.on_click_start
            #button.on_click = self.on_click_start_2(button.name,button.section,button.idx)  HOW to send argument ???
            #button.fn_on_click=emit_click
            # <<< monkey patching _____________________<<< 

            self.btn_list.append(button)
            self.h_box.add(button.with_space_around(bottom=50))
    
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
                #anchor_y="bottom",
                anchor_y="top",
                child=self.h_box)
        )

        print("\n   IconSection instanciated  \n")

    def on_draw(self):
        #self.clear()
        self.manager.draw()

    def on_click_start(self, event):
        
        print(f" {event}  {event.source}   {event.source.name}    {event.source.section}  {event.source.idx}     ")

        #self.name2fn[event.source.name]() lance la fn eponyme du btn , sans arguments  ///

        print(f"self   {self}")
        print(f"self.view   {self.view}")
        print(f"self.view.return_section_str_to_section_ref   {self.view.return_section_str_to_section_ref}")
        print(f"self.view.return_section_str_to_section_ref()   {self.view.return_section_str_to_section_ref()}")
        returned = self.view.return_section_str_to_section_ref()
        map_section_handle = returned['map_section']
        map_section_handle.add_blue_line()

        # ///////////// implem modal sur histogram bar
        returned = self.view.return_section_str_to_section_ref()
        
        #self.name2fn[event.source.name](returned['modal_section']) # key error
        self.name2fn[event.source.name](returned) # il faut descendree dans returned['modal_section'] # crash mal debug

        
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        print("mouse was pressed !")

#_______________________________________________________________________________________________


class Map(Section):
    """ This represents the place where the game takes place """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.background_color = arcade.color.BEIGE
        self.text_angle = 0
        self.time_elapsed = 0.0

        start_x = 0
        start_y = MAP_TOP_BORDER - SECURITY_NO_OVERLAP_BORDER

        self.title = arcade.Text(
            #f"Text Drawing Examples {VERSION} https://imgui-datascience.readthedocs.io/en/latest/    https://snyk.io/advisor/python/imgui/example",
            "imgui ini config was [Window][title of the tab from class Infostorage] Pos=0,600 Size=1880,299 Collapsed=0  ",
            start_x,
            start_y,
            arcade.color.NEON_GREEN,
            DEFAULT_FONT_SIZE * 2,
            width=SCREEN_WIDTH,
            align="center",
        )

        self.lines = []
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.csscolor.DIM_GRAY)
        print("\n   Map instanciated  \n")


    def add_red_line(self):
        lenght = len(self.lines)        
        new_txt = arcade.Text("Just added a new line", 80, -100*lenght + SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5,arcade.color.RED,DEFAULT_FONT_SIZE * 2,SCREEN_WIDTH,"center",)

        self.lines.append(new_txt)
        print("add_line called ,this fn is implemented in Map section")



    def add_blue_line(self):
        lenght = len(self.lines)

        txt = "Right hand icon has been clicked"
        X=0
        Y=MAP_TOP_BORDER - SECURITY_NO_OVERLAP_BORDER - DEFAULT_LINE_HEIGHT*lenght        
        new_txt = arcade.Text(txt, 0, Y, arcade.color.BLUE,DEFAULT_FONT_SIZE ,SCREEN_WIDTH,"center",)
        self.lines.append(new_txt)
        print("add_line called ,this fn is implemented in Map section")



    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        #self.clear()
        self.manager.draw()


        #imgui.new_frame() # test because only datasection appear +++

        # Draw all the text objects
        # Column 1
        self.title.draw()
        #self.fonts.draw()
        #self.font_default.draw()

        if self.lines != []:
            for line in self.lines:
                line.draw()

#_______________________________________________________________________________________________
#https://stackoverflow.com/questions/63159819/python-numpy-array-create-bar-graph-from-touple-values

#myInfostorage


class BarModalSection(Section):
    """ A modal section that represents a popup that waits for user input """

    def __init__(self, left: int, bottom: int, width: int, height: int):
        super().__init__(left, bottom, width, height, modal=True, enabled=False)

        # modal button
        self.button = arcade.SpriteSolidColor(100, 50, arcade.color.RED)
        pos = self.left + self.width / 2, self.bottom + self.height / 2
        self.button.position = pos

        self.sprite_list = arcade.SpriteList()

    def on_draw(self):
        # draw modal frame and button
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color.GRAY)
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color.WHITE)
        self.draw_button()

        # >>>>>>>>>>>>>>>>

        y= [elem[myInfostorage.pie_col_index] for elem in myInfostorage.list_of_rows]
        #y = np.array(y)
        #y = list(y)

        #copy.deepcopy()

        list_of_str = [elem[myInfostorage.pie_col_index] for elem in myInfostorage.list_of_rows]
        list_of_int = [int(elem) for elem in list_of_str]

        mylabels= [elem[1] for elem in myInfostorage.list_of_rows]

        fig,ax = plt.subplots(1, 1)

        #langs = ['C', 'C++', 'Java', 'Python', 'PHP']
        langs = ['C', 'C++', 'Java', 'Python']
        students = [28,21,14,7]



        print(" mylabels = ", mylabels)
        print(f" y =  {y}    type {type(y)}  ")


        ax.bar(mylabels,list_of_int)

        
        print(" mylabels = ", mylabels)
        print(f" y =  {y}    type {type(y)}  ") # list of string
        print(f" students =  {students}    type {type(students)}  ") # list of integers

        import base64
        from io import BytesIO        
        dynamic_path = "./dynamic_plot/"
        dynamic_file_name = "bars.png"
        fullpath = dynamic_path + dynamic_file_name
        plt.savefig(fullpath)
        print(f" plt has savefig here:   {fullpath} ")
        #import time  
        #time.sleep(1)
        #SPRITE_SCALING=1
        SPRITE_SCALING=0.75
        #print(f" before bar_sprite ")
        
        bar_sprite = arcade.Sprite(fullpath, SPRITE_SCALING)
        bar_sprite.center_x = 550
        bar_sprite.center_y = 550

        #time.sleep(1)
        
        self.sprite_list.append(bar_sprite)

        self.sprite_list.draw()

        # <<<<<<<<<<<<<<<<

    def draw_button(self):
        # draws the button and button text
        self.button.draw()
        arcade.draw_text('Close Modal', self.button.left + 5,
                         self.button.bottom + self.button.height / 2,
                         arcade.color.WHITE)

    def on_resize(self, width: int, height: int):
        """ set position on screen resize """
        self.left = width // 3
        self.bottom = (height // 2) - self.height // 2
        pos = self.left + self.width / 2, self.bottom + self.height / 2
        self.button.position = pos

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ Check if the button is pressed """
        if self.button.collides_with_point((x, y)):
            self.enabled = False




#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# https://stackoverflow.com/questions/61475603/pyimgui-with-pyglet-doubles-keyboard-input
class CellModalSection(Section):
    """ A modal section that represents a popup that waits for user input """

    def __init__(self, left: int, bottom: int, width: int, height: int):
        super().__init__(left, bottom, width, height, modal=True, enabled=False)

        # modal button
        self.button = arcade.SpriteSolidColor(100, 50, arcade.color.GOLD)
        pos = self.left + self.width / 2, self.bottom + self.height / 2
        self.button.position = pos


        self.sprite_list = arcade.SpriteList()





        self.manager = arcade.gui.UIManager() # Bar and Pie modal dont have manager ??
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
        self.input_field = arcade.gui.UIInputText(
          color=arcade.color.DARK_BLUE_GRAY,
          font_size=24,
          width=200,
          text='Hello ..')

        # Create a button
        submit_button = arcade.gui.UIFlatButton(
          color=arcade.color.DARK_BLUE_GRAY,
          text='Submit')
        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        submit_button.on_click = self.on_click 
        
        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box.add(self.label.with_space_around(bottom=0))
        #self.v_box.add(self.label.with_space_around(right=190))
        self.v_box.add(self.input_field)
        self.v_box.add(submit_button)




        #fil=arcade.draw_lrtb_rectangle_filled(95,95,95,95, arcade.color.BLUE)
        #out=arcade.draw_lrtb_rectangle_outline(35,35,35,35, arcade.color.GREEN)
        #bt=self.draw_button

        #self.v_box.add(fil)
        #self.v_box.add(out)
        #self.v_box.add(bt())


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        print(f"  dir(self.v_box)   {dir(self.v_box)}")
        print(f"  (self.v_box.parent)   {(self.v_box.parent)}")
        print(f"  (self.v_box.children)   {(self.v_box.children)}")

        #input("press enter")

    def on_draw(self):
        # draw modal frame and button
        
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                  self.bottom, arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color.GREEN)


        

        self.manager.draw()

        self.button.draw()




        #++++++$$$$$

        # https://stackoverflow.com/questions/71146065/reading-text-from-user-in-python-arcade-library

        # https://api.arcade.academy/en/latest/api/gui_widgets.html#arcade-gui-uiinputtext

        # https://stackoverflow.com/questions/57855060/i-am-making-a-text-box-in-pythons-arcade-library-i-cant-handle-the-scrolling

        # https://stackoverflow.com/questions/61398292/how-to-change-the-content-of-text-in-an-arcade-window

        # https://stackoverflow.com/questions/68118733/using-python-arcade-and-tkinter-together-hangs-the-application

        # https://github.com/eruvanos/arcade_gui



        



        

        #______________________
    def update_text(self):
        print(f"updating the label with input text '{self.input_field.text}'")
        self.label.text = self.input_field.text


    



    def draw_button(self):
        # draws the button and button text
        self.button.draw()
        arcade.draw_text('Close CellModal', self.button.left + 259,
                         self.button.bottom + self.button.height / 2,
                         arcade.color.WHITE)
        

    def on_resize(self, width: int, height: int):
        """ set position on screen resize """
        self.left = width // 3
        self.bottom = (height // 2) - self.height // 2
        pos = self.left + self.width / 2, self.bottom + self.height / 2
        self.button.position = pos

    


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ Check if the button is pressed """
        
        if self.button.collides_with_point((x, y)):
            self.enabled = False

        print("on_mouse_press from  CellModalSection")

    def on_click(self, event):
        print(f"click-event caught: {event}")
        self.update_text()


        
#////////////////////////////////////////////////////

class PieModalSection(Section):
    """ A modal section that represents a popup that waits for user input """

    def __init__(self, left: int, bottom: int, width: int, height: int):
        super().__init__(left, bottom, width, height, modal=True, enabled=False)

        # modal button
        self.button = arcade.SpriteSolidColor(100, 50, arcade.color.PURPLE)
        pos = self.left + self.width / 2, self.bottom + self.height / 2
        self.button.position = pos


        self.sprite_list = arcade.SpriteList()

    def on_draw(self):
        # draw modal frame and button
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                          self.bottom, arcade.color.ORANGE)
        arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top,
                                           self.bottom, arcade.color.PINK)
        self.draw_button()


        y= [elem[myInfostorage.pie_col_index] for elem in myInfostorage.list_of_rows]
        y = np.array(y)


        mylabels= [elem[1] for elem in myInfostorage.list_of_rows]

        plt.pie(y, labels = mylabels)

        import base64
        from io import BytesIO


        
        dynamic_path = "./dynamic_plot/"
        dynamic_file_name = "cake.png"

        fullpath = dynamic_path + dynamic_file_name
        plt.savefig(fullpath)

        print(f" plt has savefig here:   {fullpath} ")        

        #import time  
        #time.sleep(1)        

        SPRITE_SCALING=1

        print(f" before pie_sprite ")
        
        pie_sprite = arcade.Sprite(fullpath, SPRITE_SCALING)

        pie_sprite.center_x = 550
        pie_sprite.center_y = 550

        #print(dir(pie_sprite))

        #print(pie_sprite.__dict__)

        print(f" after pie_sprite ")
        #time.sleep(1)
        
        self.sprite_list.append(pie_sprite)

        self.sprite_list.draw()

        #plt.show()

        
    def draw_button(self):
        # draws the button and button text
        self.button.draw()
        arcade.draw_text('Close PieModal', self.button.left + 5,
                         self.button.bottom + self.button.height / 2,
                         arcade.color.WHITE)

    def on_resize(self, width: int, height: int):
        """ set position on screen resize """
        self.left = width // 3
        self.bottom = (height // 2) - self.height // 2
        pos = self.left + self.width / 2, self.bottom + self.height / 2
        self.button.position = pos

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """ Check if the button is pressed """
        if self.button.collides_with_point((x, y)):
            self.enabled = False

#_______________________________________________________________________________________________

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        global SCREEN_WIDTH
    

        print("\n   ---  GameView starting instanciation \n")

        self.cell_modal_section = CellModalSection(self.window.width / 3,
                                          (self.window.height / 2) - 100,
                                          350, 180)
        self.section_manager.add_section(self.cell_modal_section)





        self.bar_modal_section = BarModalSection(self.window.width / 3,
                                          (self.window.height / 2) - 100,
                                          400, 200)
        self.section_manager.add_section(self.bar_modal_section)
        print(f"7777777      class GameView(arcade.View) /init/   self.section_manager.add_section(self.bar_modal_section)   ")



        print("\n   ---  GameView starting instanciation \n")

        self.pie_modal_section = PieModalSection(self.window.width / 3,
                                          (self.window.height / 2) - 100,
                                          600, 300)
        self.section_manager.add_section(self.pie_modal_section)
        print(f"8888      class GameView(arcade.View) /init/   self.section_manager.add_section(self.pie_modal_section)   ")





        self.icon_section = IconSection (0,0 ,SCREEN_WIDTH, 299)        
        print(f" self.icon_section.__dict__     {self.icon_section.__dict__}")
        self.section_manager.add_section(self.icon_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.icon_section)   ")


        self.map_section = Map(left=0, bottom=599, width=SCREEN_WIDTH, height=290,
                            name='map_section')

        self.section_manager.add_section(self.map_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.map_section)   ")


        self.data_section = Datasec(0, 299, SCREEN_WIDTH, 290)
        self.section_manager.add_section(self.data_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.data_section)   ")

        print("\n   GameView instanciated fully accomplished  ----  \n")

        #self.section_str_to_section_ref = {"icon_section":self.icon_section,"map_section":self.map_section,"data_section":self.data_section}

        self.section_str_to_section_ref = {"icon_section":self.icon_section,
        "map_section":self.map_section,
        "data_section":self.data_section,
        "cell_modal_section":self.cell_modal_section,
        "bar_modal_section":self.bar_modal_section,       
        "pie_modal_section":self.pie_modal_section}


    def return_section_str_to_section_ref(self):

        # because of MVC pattern and having imgui rendering + arcade views to manage ... this is tricky, i share reference as i can

        return self.section_str_to_section_ref


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


"""
# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

def emit_click():
#def emit_click(event):
    #print(f" section {section}  btn {btn_name} has been clicked with interf_status {interf_status}")
    #print(f" section __  btn __ has been clicked with interf_status ___")
    #print(f" {event} ")
    print(f" fn  emit_click  just called ")

"""

"""
#++++++$$$$$

        maybemodified = 555

        imgui.new_frame()

        imgui.begin("inside CellModalSection.on_draw() => imgui.ini")
        imgui.text("foobarbazbuz")
        changed, maybemodified = imgui.input_int("Integer Input Test", maybemodified)

        print(f" changed {changed}  maybemodified {maybemodified} ")

        imgui.end()


        imgui.render()

        #______________________
"""