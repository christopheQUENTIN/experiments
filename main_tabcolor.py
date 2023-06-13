import arcade

WIDTH = 800
HEIGHT = 600
PIXEL_SIZE = 20
DRAW_GRID_LINES = True
ROWS = HEIGHT // PIXEL_SIZE
COLS = WIDTH // PIXEL_SIZE
TOOLBAR_HEIGHT = 50
FPS = 60
BG_COLOR = arcade.color.LIGHT_GRAY
BLACK = arcade.color.BLACK
RED = arcade.color.RED
GREEN = arcade.color.GREEN
BLUE = arcade.color.BLUE
WHITE = arcade.color.WHITE


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=arcade.color.BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
        if self.text:
            arcade.draw_text(self.text, self.x, self.y, self.text_color, font_size=12,
                             anchor_x="center", anchor_y="center")

    def clicked(self, x, y):
        return self.x - self.width / 2 < x < self.x + self.width / 2 and \
               self.y - self.height / 2 < y < self.y + self.height / 2


class DrawingProgram(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Drawing Program")
        self.grid = self.init_grid(ROWS, COLS, BG_COLOR)
        self.drawing_color = BLACK
        self.buttons = [
            Button(35, HEIGHT - TOOLBAR_HEIGHT / 2, 50, 50, BLACK),
            Button(95, HEIGHT - TOOLBAR_HEIGHT / 2, 50, 50, RED),
            Button(155, HEIGHT - TOOLBAR_HEIGHT / 2, 50, 50, GREEN),
            Button(215, HEIGHT - TOOLBAR_HEIGHT / 2, 50, 50, BLUE),
            Button(275, HEIGHT - TOOLBAR_HEIGHT / 2, 50, 50, WHITE, "Erase", BLACK),
            Button(335, HEIGHT - TOOLBAR_HEIGHT / 2, 50, 50, WHITE, "Clear", BLACK)
        ]
        self.current_button_index = 0

    def init_grid(self, rows, cols, color):
        grid = []
        for i in range(rows):
            grid.append([])
            for _ in range(cols):
                grid[i].append(color)
        return grid

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        for button in self.buttons:
            button.draw()

    def draw_grid(self):
        for i, row in enumerate(self.grid):
            for j, pixel in enumerate(row):
                arcade.draw_rectangle_filled(j * PIXEL_SIZE, i * PIXEL_SIZE,
                                              PIXEL_SIZE, PIXEL_SIZE, pixel)
        if DRAW_GRID_LINES:
            for i in range(ROWS + 1):
                arcade.draw_line(0, i * PIXEL_SIZE, WIDTH, i * PIXEL_SIZE, BLACK)
            for i in range(COLS + 1):
                arcade.draw_line(i * PIXEL_SIZE, 0, i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT, BLACK)

    def get_row_col_from_pos(self, x, y):
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE
        if row >= ROWS:
            raise IndexError
        return row, col

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            try:
                row, col = self.get_row_col_from_pos(x, y)
                self.grid[row][col] = self.drawing_color
            except IndexError:
                for button in self.buttons:
                    if button.clicked(x, y):
                        self.drawing_color = button.color
                        if button.text == "Clear":
                            self.grid = self.init_grid(ROWS, COLS, BG_COLOR)
                            self.drawing_color = BLACK

    def on_key_press(self, key, modifiers):
        if key == arcade.key.TAB:
            self.current_button_index = (self.current_button_index + 1) % len(self.buttons)
            self.drawing_color = self.buttons[self.current_button_index].color

    def on_update(self, delta_time):
        pass


def main():
    window = DrawingProgram(WIDTH, HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
