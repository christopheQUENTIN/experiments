import arcade
import ast
import copy   

"""
https://github.com/pythonarcade/arcade/issues/1017

https://api.arcade.academy/en/stable/examples/shape_list_demo.html
"""


# Set how many rows and columns we will have
ROW_COUNT = 100

COLUMN_COUNT = 200

# This sets the WIDTH and HEIGHT of each grid location
EDGESIZE = 10
WIDTH = EDGESIZE
HEIGHT = EDGESIZE

# This sets the margin between each cell
# and on the edges of the screen.
#MARGIN = 5
MARGIN = 0

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Buffered Example"

white = arcade.color.WHITE

red = arcade.color.RED
green = arcade.color.GREEN
blue = arcade.color.BLUE

grey = arcade.csscolor.GREY

amber = arcade.color.AMBER
ao = arcade.color.AO
champagne = arcade.color.CHAMPAGNE
yellow = arcade.color.YELLOW
violet = arcade.color.VIOLET
#grey = arcade.color.GREY
blush = arcade.color.BLUSH

bronze = arcade.color.BRONZE
wby = arcade.color.WILD_BLUE_YONDER

pale_green = arcade.csscolor.PALE_GREEN


# https://api.arcade.academy/en/stable/api/drawing_utilities.html
# https://api.arcade.academy/en/2.6.0/api/drawing_utilities.html
# https://api.arcade.academy/en/2.6.0/api/drawing_primitives.html#arcade-get-pixel

"""

arcade.get_pixel

arcade.get_pixel(x: int, y: int, components: int = 3) → Tuple[int, ...][source]

    Given an x, y, will return a color value of that point.

    Parameters

            x (int) – x location

            y (int) – y location

            components (int) – Number of components to fetch. By default we fetch 3 3 components (RGB). 4 componets would be RGBA.

    Return type

        Color


"""

#colors_list = [green,red,blue,amber,ao,champagne,yellow,violet]
#colors_list = [green,red,blue,amber,champagne,yellow,violet]
colors_list = [red,green, blue, grey, amber, champagne, yellow, blush, bronze, wby, pale_green]


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """
        super().__init__(width, height, title, fullscreen = True)

        arcade.set_background_color(arcade.color.BLACK)

        # One dimensional list of all sprites in the two-dimensional sprite list
        self.grid_sprite_list = arcade.SpriteList()

        # This will be a two-dimensional grid of sprites to mirror the two
        # dimensional grid of numbers. This points to the SAME sprites that are
        # in grid_sprite_list, just in a 2d manner.
        self.grid_sprites = []

        self.clickeds = arcade.SpriteList()

        self.registereds = arcade.SpriteList()

        #self.shape_list = arcade.SpriteList()
        self.shape_list = arcade.ShapeElementList()

        self.data_export = list()

        self.copy_mode = False

        self.loaded_datas = list()


        self.points_list = list()

        




        # Create a list of solid-color sprites to represent each grid location
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite) #whites
                self.grid_sprites[row].append(sprite) #news



        self.copy_sprite = None
        self.copylist = arcade.ShapeElementList()



    @property
    def last_idx(self):
        #if len(self.clickeds)>0:
        if len(self.points_list)>0:
            #last_idx = len(self.clickeds) - 1
            last_idx = len(self.points_list) - 1
            return last_idx
        else:
            pass



    @property
    def last_p(self):
        if len(self.clickeds)>0:
            last_point = tuple((self.clickeds[-1].center_x, self.clickeds[-1].center_y))
            return last_point
        else:
            pass


    @property
    def last_ColRow(self):
        last_point = tuple((self.clickeds[-1].center_x, self.clickeds[-1].center_y))

        column = int(self.last_p[0] // (WIDTH + MARGIN))
        row = int(self.last_p[1] // (HEIGHT + MARGIN))

        return tuple((column, row))


    @property
    def previous_color(self):

        len_shape_list = len(self.shape_list)

        if not len_shape_list == 0:
            return colors_list[len(self.shape_list) -1]

        else:
            return None


    @property
    def current_color(self):

        len_shape_list = len(self.shape_list)

        #if len_shape_list == 0:
        #    return arcade.color.GREEN
        #else:
        #    return colors_list[len(self.shape_list) -1]

        #return colors_list[len(self.shape_list) -1]
        return colors_list[len(self.shape_list)]



    @property
    def next_color(self):

        len_shape_list = len(self.shape_list)

        if not len_shape_list >= len(colors_list):
            return colors_list[len(self.shape_list) +1]

        else:
            return None


    def setup(self):

       pass
    

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.grid_sprite_list.draw()


        



        arcade.draw_text(f" SCREEN_WIDTH {SCREEN_WIDTH} ; SCREEN_HEIGHT {SCREEN_HEIGHT}  ", SCREEN_WIDTH//2, SCREEN_HEIGHT - 50,arcade.color.RED, 17, width=25, align="center")
        arcade.draw_text(f" previous_color = {self.previous_color}   Activ color = {self.current_color}   next color = {self.next_color}   ", SCREEN_WIDTH//10, SCREEN_HEIGHT - 120,arcade.color.BLACK, 17, width=25, align="left")

        #colors_list
        #arcade.draw_text(f" self.last_p {self.last_p} ", SCREEN_WIDTH//16, 90,arcade.color.ORANGE, 17, width=25, align="left")
        arcade.draw_text(f" self.points_list {self.points_list} ", SCREEN_WIDTH//16, 90,arcade.color.ORANGE, 17, width=25, align="left")

        if len(self.clickeds) > 0:

            X_pix = self.last_p[0]
            Y_pix = self.last_p[1]

            pixelcolor = arcade.get_pixel(x=self.last_p[0], y=self.last_p[1], components = 3)
            #pixelcolor_with_alpha = arcade.make_transparent_color(pixelcolor, 0.9)
            pixelcolor_with_alpha = arcade.make_transparent_color(pixelcolor, 50)

            arcade.draw_text(f" {self.last_p} {self.last_ColRow}  ", 1700, 500,arcade.color.YELLOW, 17, width=25, align="center")

            arcade.draw_text(f" {pixelcolor}  ", 1700, 500-200,arcade.color.YELLOW, 17, width=20, align="center")

            arcade.draw_text(f" {pixelcolor_with_alpha}  ", 1700, 500-300,arcade.color.YELLOW, 17, width=20, align="center")
            arcade.draw_text(f" self.last_idx {self.last_idx}  ", 1700, 500-400,arcade.color.PINK, 17, width=20, align="center")


            

            #vert_line = arcade.draw_line(X_pix, 0, X_pix, SCREEN_HEIGHT, arcade.color.BLACK, 2)
            #horiz_line = arcade.draw_line(0, Y_pix, SCREEN_WIDTH, Y_pix, arcade.color.BLACK, 2)

            #vert_line = arcade.draw_line(X_pix, 0, X_pix, SCREEN_HEIGHT, pixelcolor, EDGESIZE)
            vert_line = arcade.draw_line(X_pix, 0, X_pix, SCREEN_HEIGHT, pixelcolor_with_alpha, EDGESIZE)
            
            #horiz_line = arcade.draw_line(0, Y_pix, SCREEN_WIDTH, Y_pix, (125,125,125,50), EDGESIZE)
            horiz_line = arcade.draw_line(0, Y_pix, SCREEN_WIDTH, Y_pix, pixelcolor_with_alpha, EDGESIZE)



        if len(self.shape_list) > 0:
            self.shape_list.draw()

        if self.copy_mode is True:
            
            if len(self.copylist) > 0:
                

                self.copylist.draw()



    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        #X_clean = column * (WIDTH + MARGIN)
        #Y_clean = row * (HEIGHT + MARGIN)

        X_clean = column * (WIDTH + MARGIN) +0.5*EDGESIZE # because finally we display sprite with center instead of bottomleft
        Y_clean = row * (HEIGHT + MARGIN) +0.5*EDGESIZE

        

        coord = tuple((x, y))
        coord_clean = tuple((X_clean, Y_clean))

        #if coord not in self.points_list:
        if coord_clean not in self.points_list:
            #self.points_list.append(coord)
            self.points_list.append(coord_clean)


            # Make sure we are on-grid. It is possible to click in the upper right
            # corner in the margin and go to a grid location that doesn't exist
            if row < ROW_COUNT and column < COLUMN_COUNT:
            
                if self.grid_sprites[row][column].color == arcade.color.WHITE: # Flip the location between 1 and 0.
                    self.grid_sprites[row][column].color = self.current_color #self.grid_sprites[row][column].color = arcade.color.GREEN
                    self.clickeds.append(self.grid_sprites[row][column])


        else:
            new_point_list = copy.deepcopy(self.points_list)
            #idx_double = new_point_list.index(coord)
            idx_double = new_point_list.index(coord_clean)

            del new_point_list[idx_double]
            self.points_list = new_point_list


            #del self.grid_sprite_list[idx_double]
            # self.grid_sprite_list
            # self.last_idx

            #self.last_ColRow dernier pas forcement le clicked si milieu de list par ex


            #self.grid_sprites[row][column].color == arcade.color.WHITE
            x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)           # risk micro overlap selon / ou //
            y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
            sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
            sprite.center_x = x
            sprite.center_y = y
            self.grid_sprite_list.append(sprite) #whites
            self.grid_sprites[row].append(sprite) #news  # IndexError: list index out of range if click out of the grid



        #self.points_list.append(coord) !!!!!§§§§


        



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.ESCAPE:
            #self.grid_sprite_list.pop()
            arcade.exit()



        if key == arcade.key.UP:
            #self.grid_sprite_list.pop()

            last_ColRowlicked = self.clickeds[-1]

            for grigri in self.grid_sprite_list:
                if grigri == last_ColRowlicked:
                    grigri.color = arcade.color.WHITE



            self.clickeds.pop()

            

        


        if key == arcade.key.SPACE:

            if len(self.points_list) >= 2:


                print(f"  self.registereds {self.registereds}   len {len(self.registereds)}  ")

                for registar in self.registereds:
                    print(f" -registar  {registar} ")


                self.registereds.append(self.clickeds[-2]) # keep the double pixel click in memory instead of cancel erase doublon
                self.registereds.append(self.clickeds[-1])


                reg0 = self.registereds[0]
                reg1 = self.registereds[1]

                print(f" ____reg0  {reg0} ")
                print(f" reg1  {reg1} ")

                
                print(f"  self.points_list[-2] {self.points_list[-2]}     ")
                print(f"  self.points_list[-1] {self.points_list[-1]}     ")

                print(f"  self.registereds {self.registereds}     len {len(self.registereds)}  ")

                for registar in self.registereds:
                    print(f" -registar  {registar} ")

                print(f"  reg0 {reg0}    reg1 {reg1} ")

                                
                current_rect = arcade.create_rectangle_filled(reg0.center_x +0.5*abs(reg1.center_x - reg0.center_x), reg0.center_y -0.5*abs(reg0.center_y - reg1.center_y), abs(reg1.center_x - reg0.center_x), abs(reg0.center_y - reg1.center_y), color=self.current_color)

                self.shape_list.append(current_rect)

                print(f"  self.shape_list  {self.shape_list}    {len(self.shape_list)}    ")

                self.clickeds = self.clickeds[2:]

                self.registereds = self.registereds[2:]


                print(f"current_rect  {current_rect} ")

                print(f"current_rect.__dict__  {current_rect.__dict__} ")

                print("\n\n\n")
                print("------------------------------------------")

                print(f" reg0.center_x  {reg0.center_x}  reg0.center_y  {reg0.center_y} ")
                print(f"                                                                                    reg1.center_x  {reg1.center_x}  reg1.center_y  {reg1.center_y} ")
                print(f" width  {abs(reg1.center_x - reg0.center_x)}  height  {abs(reg0.center_y - reg1.center_y)} ")
                print(f" self.current_color  {self.current_color} ")
                print("\n\n\n")

                rectx = reg0.center_x
                recty = reg0.center_y

                width = abs(reg1.center_x - reg0.center_x)
                height = abs(reg0.center_y - reg1.center_y)

                #rect_export = tuple((rectx, recty, width, height))
                #rect_export = tuple((rectx, recty, width, height, self.current_color))
                rect_export = tuple((rectx, recty, width, height, self.previous_color))


                print(f" rect_export  {rect_export}")
                self.data_export.append(rect_export)

                print(f" self.data_export  {self.data_export}")
                




    def on_key_release(self, key, modifiers):


        if key == arcade.key.C:

            print(f"  self.copy_mode = {self.copy_mode}   ")

            self.copy_mode = True

            self.copylist.append(self.shape_list[-1])


        if key == arcade.key.ENTER:

            #print(f"  self.copy_mode = {self.copy_mode}   ")

            newfile = "./exportfiles/rects.txt"

            with open(newfile, 'w') as outfile:
                outfile.write(str(self.data_export))
                
                #for rect in self.data_export:
                    #outfile.write(rect)         # TypeError: write() argument must be str, not tuple
                    #outfile.write(str(rect))

        if key == arcade.key.L:

            #print(f"  self.copy_mode = {self.copy_mode}   ")

            savfile = "./exportfiles/rects.txt"

            with open(savfile, 'r') as infile:
                infile_content = infile.read().split('\n')
                print(f" infile_content = {infile_content}    type {type(infile_content)}")

                #self.loaded_datas = ast.literal_eval(infile_content)    # ['(305.0, 895.0, 280.0, 300.0, (255, 0, 0))(605.0, 885.0, 410.0, 110.0, (0, 0, 255))(605.0, 765.0, 400.0, 170.0, (255, 191, 0))(315.0, 585.0, 710.0, 370.0, (0, 128, 0))(1045.0, 875.0, 520.0, 670.0, (247, 231, 206))']
                self.loaded_datas = ast.literal_eval(infile_content[0])

                for rect in self.loaded_datas:
                    current_rect = arcade.create_rectangle_filled(*rect)
                    self.shape_list.append(current_rect)



            






    def on_mouse_motion(self, x, y, dx, dy):





        if len(self.copylist) >0:
            self.copylist[-1].center_x = x
            self.copylist[-1].center_y = y



def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()