import arcade
import arcade.gui
from arcade import Section

from typing import Optional
from math import sqrt


import imgui
from arcade_imgui import ArcadeRenderer
import arcade_imgui

MAP_TOP_BORDER = 599
MAP_BOT_BORDER = 300



SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

DEFAULT_FONT_SIZE = 10

DEFAULT_LINE_HEIGHT = DEFAULT_FONT_SIZE * 3

SECURITY_NO_OVERLAP_BORDER = DEFAULT_LINE_HEIGHT * 2


# https://api.arcade.academy/en/latest/examples/sections_demo_3.html#sections-demo-3
# https://api.arcade.academy/en/development/programming_guide/sections.html


# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=arcade.gui.UITextureButton#arcade.gui.UITextureButton

# https://api.arcade.academy/en/latest/api/gui_widgets.html?highlight=arcade.gui.UITextureButton#arcade.gui.UIAnchorWidget

# https://api.arcade.academy/en/latest/examples/gui_flat_button.html#gui-flat-button


# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()



from typing import List



class Infostorage():

    def __init__(self):
        self.name_of_table_imgui: str = ""
        self.list_col_names = [str]
        self.list_of_rows: List[List[str]]

    def test_setup(self):
        self.name_of_table_imgui = "title of the tab from class Infostorage"
        self.list_col_names = ["ID", "File", "Size", "Last modified"]
        self.list_of_rows = [['FileA.txt','99957 Kb', '12th Feb, 2016 12:19:01'],['ImageQ.png', '349 Kb', '1st Mar, 2016 06:38:22']]

    def fillupjam(self):

        jamrow = ['6564646', 'shfsgjjdsfh', 'XYZWH']
        self.list_of_rows.append(jamrow)

    def largerjam(self):

        jamcol = "A_B_C"
        self.list_col_names.append(jamcol)



myInfostorage = Infostorage()
myInfostorage.test_setup()

#class MyWindow(arcade.Window):
class IconSection(Section):

    def on_click_start(self, event):
        print("Start:", event)

    def on_click_buttonTXR(self, event):
        print("on_click_buttonTXR  clicked:", event)

    def on_draw(self):
        #self.clear()
        self.manager.draw()


    def on_click___add_row(self, event):
        print("add_row:  ", event)
        self.view.map_section.add_red_line()




    def on_click___add_column(self, event):
        print("add_column:  ", event)

    def on_click___subset_rows(self, event):
        print("subset_rows:  ", event)

    def on_click___subset_cols(self, event):
        print("subset_cols:  ", event)


    def on_click___look_db(self, event):
        print("look_db:  ", event)

    def on_click___cell(self, event):
        print("cell:  ", event)

    def on_click___bar(self, event):
        print("bar:  ", event)

    def on_click___pie(self, event):
        print("pie:  ", event)

    def on_click___ascdes(self, event):
        print("ascdes:  ", event)

        myInfostorage.largerjam()
        print("JUST CALLED myInfostorage.largerjam() FROM on_click___ascdes  ", event)

        

    def on_click___var(self, event):
        print("var:  ", event)
        self.view.map_section.add_blue_line()
        print("debug gps   self.on_click___var  ", event)

        myInfostorage.fillupjam()
        print("JUST CALLED myInfostorage.fillupjam() FROM on_click___var  ", event)


    def __init__(self, left: int, bottom: int, width: int, height: int,
             **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.ALMOND)


        self.h_box = arcade.gui.UIBoxLayout(x=0, y=0, vertical=False)


        self.fn_list = [self.on_click___add_row,self.on_click___add_column,self.on_click___subset_rows,self.on_click___subset_cols,self.on_click___look_db,self.on_click___cell,self.on_click___bar,self.on_click___pie,self.on_click___ascdes, self.on_click___var]

        dico_fn_triplettes = {self.on_click___add_row: ("add_row_btn_idle.png", "add_row_btn_hovered.png", "add_row_btn_clicked.png")}
        dico_fn_triplettes.update({self.on_click___add_column: ("add_column_btn_idle.png","add_column_btn_hovered.png","add_column_btn_clicked.png")})


        dico_fn_triplettes.update({self.on_click___subset_rows: ("subset_rows_idle.png", "subset_rows_hovered.png", "subset_rows_clicked.png")})
        dico_fn_triplettes.update({self.on_click___subset_cols: ("subset_cols_idle.png", "subset_cols_hovered.png", "subset_cols_clicked.png")})
        

        dico_fn_triplettes.update({self.on_click___look_db: ("look_db_idle.png", "look_db_hovered.png", "look_db_clicked.png")})

        dico_fn_triplettes.update({self.on_click___cell: ("cell_idle.png", "cell_hovered.png", "cell_clicked.png")})
        dico_fn_triplettes.update({self.on_click___bar: ("bar_idle.png", "bar_hovered.png", "bar_clicked.png")})

        dico_fn_triplettes.update({self.on_click___pie: ("pie_idle.png", "pie_hovered.png", "pie_clicked.png")})

        dico_fn_triplettes.update({self.on_click___ascdes: ("ascdes_idle.png", "ascdes_hovered.png", "ascdes_clicked.png")})
        dico_fn_triplettes.update({self.on_click___var: ("var_idle.png", "var_hovered.png", "var_clicked.png")})

        


        print("dico_fn_triplettes ",dico_fn_triplettes)  
        print("\n\n ---------------------- \n\n")
 

        i=0

        for k,v in dico_fn_triplettes.items():
            #foo_txr + '_idle', foo_txr + '_idle', foo_txr + '_idle' = arcade.load_texture(f"./icons/{foo_txr}+ '_idle'")

            button = arcade.gui.UITextureButton(x=100, y=50, 
                texture=arcade.load_texture(f"./icons/{v[0]}"),
                texture_hovered=arcade.load_texture(f"./icons/{v[1]}"),
                texture_pressed=arcade.load_texture(f"./icons/{v[2]}"))

            button.on_click = self.fn_list[i]

            


            self.h_box.add(button.with_space_around(bottom=50))
            i += 1




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




class Map(Section):
    """ This represents the place where the game takes place """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.background_color = arcade.color.BEIGE
        self.text_angle = 0
        self.time_elapsed = 0.0

        # Add the screen title
        start_x = 0
        #start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        #start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT 

        start_y = MAP_TOP_BORDER - SECURITY_NO_OVERLAP_BORDER




        



        self.title = arcade.Text(
            "Text Drawing Examples https://imgui-datascience.readthedocs.io/en/latest/    https://snyk.io/advisor/python/imgui/example",
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
        #new_txt = arcade.Text("Text Drawing Examples", start_x=80,
        #    start_y= 900-50*lenght,arcade.color.NEON_GREEN,DEFAULT_FONT_SIZE * 2,width=SCREEN_WIDTH,align="center",)
        
        #new_txt = arcade.Text("Text Drawing Examples", 80, 900-50*lenght,arcade.color.NEON_GREEN,DEFAULT_FONT_SIZE * 2,SCREEN_WIDTH,"center",)
        new_txt = arcade.Text("Just added a new line", 80, -100*lenght + SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5,arcade.color.RED,DEFAULT_FONT_SIZE * 2,SCREEN_WIDTH,"center",)

        self.lines.append(new_txt)


        print("add_line called ,this fn is implemented in Map section")

        #-100*lenght + SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5


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




        

        #imgui.new_frame()
        #imgui.begin("Mi primera ventana", True)
        #imgui.text("Hola Mundo")
        #imgui.end()
        #imgui.render()





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


    def on_draw_rows(self, list_of_rows: str):

        imgui.set_column_offset(1, 40)
        imgui.next_column()

        for row in list_of_rows:
            for cell in row:

                imgui.text(cell)
                imgui.next_column()



                
            imgui.next_column()
        
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
        

        

        #imgui.render() # optionel
        #self.renderer.render(imgui.get_draw_data())   AttributeError: 'Datasec' object has no attribute 'renderer'


#________________________    

class GameView(arcade.View):
    """ The game itself """

    def __init__(self):
        super().__init__()


        print("\n   ---  GameView starting instanciation \n")

        # create and store the modal, so we can set
        # self.modal_section.enabled = True to show it
        self.icon_section = IconSection (0,0,SCREEN_WIDTH, 299)


        self.map_section = Map(0, 300, SCREEN_WIDTH, 299)


        self.data_section = Datasec(0, 600, SCREEN_WIDTH, 299)

        # add the sections
        self.section_manager.add_section(self.icon_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.icon_section)   ")


        self.section_manager.add_section(self.map_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.map_section)   ")



        self.section_manager.add_section(self.data_section)
        print(f"class GameView(arcade.View) /init/   self.section_manager.add_section(self.data_section)   ")



        print("\n   GameView instanciated fully accomplished  ----  \n")



    def on_draw(self):
        arcade.start_render()

        #self.renderer.render(imgui.get_draw_data())  # AttributeError: 'GameView' object has no attribute 'renderer'




class SpecialWindow(arcade.Window):

    def __init__(self):
        
        super().__init__(1900, 960, "init SpecialWindow Basic Example", resizable=True)

        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

        print("\n   SpecialWindow instanciated  \n")


    def on_draw(self):
        #self.clear()
        #imgui.render()
        self.renderer.render(imgui.get_draw_data())   # self.renderer = impl notebook , que du rose si comment

        #arcade.finish_render()

def give_me_a_special_window():
    special_window = SpecialWindow()

    return special_window


def main():
    
    window = give_me_a_special_window()

    window.clear()

    print(f"main=>  class SpecialWindow(arcade.Window) /init/   window = give_me_a_special_window()   ")

    game = GameView()

    window.show_view(game)

    window.run()


if __name__ == '__main__':
    main()















"""


import arcade
import imgui
from arcade_imgui import ArcadeRenderer
import arcade_imgui


class BasicExample(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Basic Example", resizable=True)

        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

    def on_draw(self):
        self.clear()

        imgui.new_frame()

        imgui.begin("Example: Columns - File list")
        imgui.columns(4, 'fileLlist')
        imgui.separator()
        imgui.text("ID")
        imgui.next_column()
        imgui.text("File")
        imgui.next_column()
        imgui.text("Size")
        imgui.next_column()
        imgui.text("Last Modified")
        imgui.next_column()
        imgui.separator()
        imgui.set_column_offset(1, 40)

        imgui.next_column()
        imgui.text('FileA.txt')
        imgui.next_column()
        imgui.text('57 Kb')
        imgui.next_column()
        imgui.text('12th Feb, 2016 12:19:01')
        imgui.next_column()

        imgui.next_column()
        imgui.text('ImageQ.png')
        imgui.next_column()
        imgui.text('349 Kb')
        imgui.next_column()
        imgui.text('1st Mar, 2016 06:38:22')
        imgui.next_column()

        imgui.columns(1)
        imgui.end()


        imgui.render()
        self.renderer.render(imgui.get_draw_data())


if __name__ == '__main__':
    window = BasicExample()
    arcade.run()



"""