# imports

#   gui imports

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, \
    QPushButton, QMessageBox, QLabel, QInputDialog, QLineEdit
import os
import ast
import json

#   game imports

import pygame
import random

"""
    Block class, represents a block in game
    four blocks form a shape
"""


class Block:

    # Constructor
    def __init__(self, x=0, y=0, color=(0, 0, 255)):

        # X, Y position of block on map

        self.x = x
        self.y = y

        self.color = color

        # is_moving helps to determine if grid should has '1' in place of block

        self.is_moving = True

        # is_active says if this block is the active one
        #    ( the one that is being moved by player )

        self.is_active = True

        # is_alive is set False when block is removed from the game
        #    ( by removing full row )

        self.is_alive = True


"""
    Shape class, represents a shape made
    from four blocks, it contains
    shapes function like rotate(args)
"""


class Shape:

    # Constructor
    #    block_i are blocks that this shape is made from
    #    shape is this shapes number used for getting blocks
    #    positions from shapes list
    #    every shape has one, two or four rotations
    #    rotation_counter keeps track of it
    #    is_active helps to fix some time errors
    def __init__(self, block_one, block_two, block_three, block_four, shape, rotation_counter=0):
        self.block_one = block_one
        self.block_two = block_two
        self.block_three = block_three
        self.block_four = block_four
        self.shape = shape
        self.rotation_counter = rotation_counter
        self.is_active = True

    # function that 'rotates' a shape
    #    shapes is list of shapes
    #    re_rotate says if function is used for rotating
    #    or canceling rotation ( in case of rotating
    #    being not possible in first place
    def rotate(self, shapes, re_rotate):

        if not re_rotate:

            # ----- repairing position of shape on map ----- #

            if self.shape == 0:
                if self.rotation_counter == 1:
                    self.block_one.x -= 1
                else:
                    self.block_one.x += 1

            elif self.shape == 1:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                elif self.rotation_counter == 2:
                    self.block_one.x += 1
                elif self.rotation_counter == 3:
                    self.block_one.x -= 1
                else:
                    self.block_one.x -= 1

            elif self.shape == 3:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                elif self.rotation_counter == 2:
                    self.block_one.x -= 1
                elif self.rotation_counter == 3:
                    self.block_one.x -= 1
                else:
                    self.block_one.x += 1

            elif self.shape == 4:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                elif self.rotation_counter == 2:
                    self.block_one.x -= 1
                elif self.rotation_counter == 3:
                    self.block_one.x -= 1
                else:
                    self.block_one.x += 1

            elif self.shape == 5:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                else:
                    self.block_one.x -= 1

            elif self.shape == 6:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                else:
                    self.block_one.x -= 1

            # ----- rotating ----- #

            self.block_two.x = self.block_one.x + shapes[self.shape][self.rotation_counter][0]
            self.block_two.y = self.block_one.y + shapes[self.shape][self.rotation_counter][1]
            self.block_three.x = self.block_one.x + shapes[self.shape][self.rotation_counter][2]
            self.block_three.y = self.block_one.y + shapes[self.shape][self.rotation_counter][3]
            self.block_four.x = self.block_one.x + shapes[self.shape][self.rotation_counter][4]
            self.block_four.y = self.block_one.y + shapes[self.shape][self.rotation_counter][5]

            # managing rotation_counter

            if len(shapes[self.shape]) > self.rotation_counter + 1:
                self.rotation_counter += 1
            else:
                self.rotation_counter = 0

        else:

            # managing ( correcting ) rotation_counter

            if self.rotation_counter == 1:
                self.rotation_counter = len(shapes[self.shape]) - 1

            elif self.rotation_counter > 1:
                self.rotation_counter -= 2

            else:
                self.rotation_counter = len(shapes[self.shape]) - 2

            # ----- repairing position of shape on map ----- #

            if self.shape == 0:
                if self.rotation_counter == 1:
                    self.block_one.x -= 1
                else:
                    self.block_one.x += 1

            elif self.shape == 1:
                if self.rotation_counter == 1:
                    self.block_one.x -= 1
                elif self.rotation_counter == 2:
                    self.block_one.x += 1
                elif self.rotation_counter == 3:
                    self.block_one.x += 1
                else:
                    self.block_one.x -= 1
                    self.block_one.y -= 1

            elif self.shape == 3:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                elif self.rotation_counter == 2:
                    self.block_one.x += 1
                elif self.rotation_counter == 3:
                    self.block_one.x -= 1
                else:
                    self.block_one.x -= 1

            elif self.shape == 4:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                elif self.rotation_counter == 2:
                    self.block_one.x += 1
                elif self.rotation_counter == 3:
                    self.block_one.x -= 1
                else:
                    self.block_one.x -= 1

            elif self.shape == 5:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                else:
                    self.block_one.x -= 1

            elif self.shape == 6:
                if self.rotation_counter == 1:
                    self.block_one.x += 1
                else:
                    self.block_one.x -= 1

            # ----- rotating ----- #

            self.block_two.x = self.block_one.x + shapes[self.shape][self.rotation_counter][0]
            self.block_two.y = self.block_one.y + shapes[self.shape][self.rotation_counter][1]
            self.block_three.x = self.block_one.x + shapes[self.shape][self.rotation_counter][2]
            self.block_three.y = self.block_one.y + shapes[self.shape][self.rotation_counter][3]
            self.block_four.x = self.block_one.x + shapes[self.shape][self.rotation_counter][4]
            self.block_four.y = self.block_one.y + shapes[self.shape][self.rotation_counter][5]

            # managing rotation_counter

            if len(shapes[self.shape]) > self.rotation_counter + 1:
                self.rotation_counter += 1
            else:
                self.rotation_counter = 0

    # Function moves every shapes block with given
    # X, Y values
    def move_shape(self, x, y):
        self.block_one.x += x
        self.block_one.y += y
        self.block_two.x += x
        self.block_two.y += y
        self.block_three.x += x
        self.block_three.y += y
        self.block_four.x += x
        self.block_four.y += y


"""
    Main class, generates GUI and game when needed,
    game loop, all game and menu functions are here
"""


class Menu:

    # Constructor
    def __init__(self):

        # ----- Creating application, main window and main layout ----- #

        self.app = QApplication([])
        self.window = QWidget()
        self.window.setFixedSize(250, 500)
        self.window.setWindowTitle("Tetris v3.0")
        main_layout = QVBoxLayout()
        self.window.setLayout(main_layout)

        # preparing dict for high scores

        self.scores = {}

        self.name = ''

        # ----- Creating buttons and setting their attributes ----- #
        #           ( using helper function )                       #

        self.start = QPushButton("Start!")
        self.rules = QPushButton("Rules")
        self.high_scores = QPushButton("High scores")
        self.author = QPushButton("Author")
        self.end = QPushButton("Quit")

        self.init_buttons(main_layout)

        self.add_image(main_layout, "main_layout_icon.png")

        # ----- initialization of variables that are used later ----- #

        # Variables needed to print score
        pygame.init()
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.my_string = 'Score: 0'
        self.text = self.font.render(self.my_string, True, (0, 255, 0), (0, 0, 128))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (100, 12)
        # Music
        pygame.mixer.init()
        pygame.mixer_music.load('song.mp3')
        pygame.mixer_music.play(-1)
        # Says if game is running
        self.running = False
        # Active shape ( the one moving )
        self.active_shape = None
        # Time managing variable
        self.time_counter = 5999
        self.blocks = []
        # All shapes are stored in this list
        self.shapes = []
        # Game grid
        self.grid = self.create_grid()
        # Game window
        self.width = 480
        self.height = 720
        self.screen = None
        # Size that is actually used for the game
        self.p_width = 300
        self.p_height = 600
        # Helper variables that are X, Y position of left top corner
        self.top_left_x = (self.width - self.p_width) // 2
        self.top_left_y = (self.height - self.p_height) // 2
        # Size of block on screen
        self.block_size = 30
        # Grid size
        self.rows = 20
        self.columns = 10
        # List of colors (RGB)
        self.colors = [(255, 255, 255),     # White
                       (0, 0, 255),         # Blue
                       (0, 255, 0),         # Green
                       (255, 255, 0),       # Yellow
                       (0, 255, 255),       # Light blue
                       (255, 0, 255),       # Purple
                       (128, 0, 128)]       # Pink
        # Shape representations, each shape starts with one block, and then
        #   three more blocks are added with position that is equal to
        #   position of first block +/- two numbers ( X, Y ) from list
        #   ( there are 3 "pairs" for each block )
        #   shapes have different possible rotations number hence different
        #   lists lengths.
        self.i_shape = [[0, 1, 0, 2, 0, 3], [1, 0, 2, 0, 3, 0]]
        self.t_shape = [[1, 0, 2, 0, 1, 1], [0, 1, 0, 2, -1, 1], [-1, 0, -2, 0, -1, -1], [0, -1, 0, -2, 1, -1]]
        self.o_shape = [[1, 0, 0, 1, 1, 1]]
        self.l_shape = [[0, 1, 0, 2, 1, 2], [-1, 0, -2, 0, -2, 1], [0, -1, 0, -2, -1, -2], [1, 0, 2, 0, 2, -1]]
        self.j_shape = [[0, 1, 0, 2, -1, 2], [-1, 0, -2, 0, -2, -1], [0, -1, 0, -2, 1, -2], [1, 0, 2, 0, 2, 1]]
        self.s_shape = [[1, 0, 1, -1, 2, -1], [0, -1, 1, 0, 1, 1]]
        self.z_shape = [[1, 0, 1, 1, 2, 1], [0, 1, -1, 1, -1, 2]]
        # List of these shapes
        self.shape_types = [self.i_shape, self.t_shape, self.o_shape,
                            self.l_shape, self.j_shape, self.s_shape, self.z_shape]

        # Players points
        self.points = 0
        # If multiple rows get deleted player gets more points
        self.multiplier = 0

        self.window.show()
        self.app.exec_()

    # -------------------------------------------------------------------- #
    # ------------------------- button functions ------------------------- #
    # -------------------------------------------------------------------- #

    def start_clicked(self):
        self.game_init()
        self.run()

    # Function loads high scores from file and displays it in message box
    def high_scores_clicked(self):
        self.load_scores()
        reversed_dict = {}
        scores_list = list(self.scores)
        scores_list.reverse()
        for key in scores_list:
            reversed_dict[key] = self.scores.get(key)
        self.scores = reversed_dict
        if len(self.scores) == 11:
            self.scores.popitem()
        scores_str = "\n".join("{!r}: {!r},".format(k, v) for k, v in self.scores.items())
        msg = QMessageBox()
        msg.setWindowTitle("High scores:")
        msg.setText(scores_str)
        msg.exec_()

    def rules_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Rules:")
        msg.setText("During the game, new shapes appear on the top of the game area.\n"
                    "Every shape is made of four blocks.\n"
                    "Shapes are moving down with constant speed.\n"
                    "When shape touches bottom of the map or gets blocked\n"
                    "by another shape beneath him it stops moving\n"
                    "and new shape is created.\n"
                    "Game lasts till there is no place for new shape.\n"
                    "Player has to move and rotate shapes\n"
                    "in such way as to fill the rows,\n"
                    "full rows disappear granting points.\n"
                    "Controls:\n"
                    "   A - move shape left\n"
                    "   D - move shape right\n"
                    "   S - move shape faster\n"
                    "   R - rotate shape")
        msg.exec_()

    def author_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("Info about the author:")
        msg.setText("Author: Kacper Sarzynski")
        msg.exec_()

    def end_clicked(self):
        exit()

    # -------------------------------------------------------------------- #
    # -------------------------- Game functions -------------------------- #
    # -------------------------------------------------------------------- #

    # Main game function, it contains main games loop
    #    and initializes games attributes
    def run(self):
        self.game_init()
        self.running = True
        while self.running:
            # first, events are processed
            self.event_handling()
            # then changes are made
            self.logic()
            # finally game window is updated
            self.update()

    # Function that checks if shape fits on the map and if it doesnt
    #    overlaps another shape
    #    shape argument is saying for which shape object
    #    are we checking if its okay
    #    rotated says if we check shape after it was rotated or just
    #    moved by player
    #    in first case we re-rotate our shape and return True
    #    in second we just return False
    #    grid is game grid ( used to check if shape overlaps another )
    def is_shape_ok(self, shape, rotated, grid):
        if rotated:
            if shape.block_one.x < 3 or shape.block_one.x > 12 or \
                    shape.block_one.y < 3 or shape.block_one.y > 22 or \
                    grid[shape.block_one.y][shape.block_one.x] == 1:
                shape.rotate(self.shape_types, True)
                return True
            elif shape.block_two.x < 3 or shape.block_two.x > 12 or \
                    shape. block_two.y < 3 or shape.block_two.y > 22 or \
                    grid[shape.block_two.y][shape.block_two.x] == 1:
                shape.rotate(self.shape_types, True)
                return True
            elif shape.block_three.x < 3 or shape.block_three.x > 12 or \
                    shape.block_three.y < 3 or shape.block_three.y > 22 or \
                    grid[shape.block_three.y][shape.block_three.x] == 1:
                shape.rotate(self.shape_types, True)
                return True
            elif shape.block_four.x < 3 or shape.block_four.x > 12 or \
                    shape.block_four.y < 3 or shape.block_four.y > 22 or \
                    grid[shape.block_four.y][shape.block_four.x] == 1:
                shape.rotate(self.shape_types, True)
                return True
        else:
            if shape.block_one.x < 3 or shape.block_one.x > 12 or \
                    shape.block_one.y < 3 or shape.block_one.y > 22 or \
                    grid[shape.block_one.y][shape.block_one.x] == 1:
                return False
            elif shape.block_two.x < 3 or shape.block_two.x > 12 or \
                    shape.block_two.y < 3 or shape.block_two.y > 22 or \
                    grid[shape.block_two.y][shape.block_two.x] == 1:
                return False
            elif shape.block_three.x < 3 or shape.block_three.x > 12 or \
                    shape.block_three.y < 3 or shape.block_three.y > 22 or \
                    grid[shape.block_three.y][shape.block_three.x] == 1:
                return False
            elif shape.block_four.x < 3 or shape.block_four.x > 12 or \
                    shape.block_four.y < 3 or shape.block_four.y > 22 or \
                    grid[shape.block_four.y][shape.block_four.x] == 1:
                return False
        return True

    # Function manages events
    def event_handling(self):

        for event in pygame.event.get():

            # Quit event
            if event.type == pygame.QUIT:
                self.running = False

            # Any button pressed
            if event.type == pygame.KEYDOWN:

                # 'A' pressed
                if event.key == pygame.K_a:
                    self.active_shape.move_shape(-1, 0)
                    if not self.is_shape_ok(self.active_shape, False, self.grid):
                        self.active_shape.move_shape(1, 0)

                # 'D' pressed
                elif event.key == pygame.K_d:
                    self.active_shape.move_shape(1, 0)
                    if not self.is_shape_ok(self.active_shape, False, self.grid):
                        self.active_shape.move_shape(-1, 0)

                # 'R' pressed
                elif event.key == pygame.K_r:
                    self.active_shape.rotate(self.shape_types, False)
                    # I check if rotation was possible
                    #    if it wasn't i re-rotate my shape
                    self.is_shape_ok(self.active_shape, True, self.grid)

                # -------- testing --------- #
                # 'P' pressed
                elif event.key == pygame.K_p:
                    self.active_shape.rotate(self.shape_types, True)
                    # I check if re-rotation was possible
                    #    if it wasn't i rotate my shape
                    self.is_shape_ok(self.active_shape, False, self.grid)
                # ----- testing  ended ----- #

                # 'S' pressed
                elif event.key == pygame.K_s:
                    self.active_shape.move_shape(0, 1)
                    if not self.is_shape_ok(self.active_shape, False, self.grid):
                        self.active_shape.move_shape(0, -1)

    # Function that updates window
    def update(self):

        # Clearing window
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.height))
        # Drawing blocks
        for block in self.blocks:
            if block.is_alive:
                pygame.draw.rect(self.screen, block.color,
                                 (self.top_left_x + (block.x - 3) * self.block_size,
                                  self.top_left_y + (block.y - 3) * self.block_size,
                                  self.block_size, self.block_size))

        # Drawing grid
        self.draw_grid()

        pygame.display.update()

    # Function that calculates everything,
    # in other words its responsible for game working
    def logic(self):
        # Updating grid
        self.update_grid()
        # Managing of adding new shapes
        #    this function also checks if game is over
        self.add_shape()
        # Checking if game is over
        self.is_game_over()
        # Managing moving active shape
        #    ( checking if it should be moved and moving )
        self.move_active_shape()
        # Deleting full rows ( if there are full rows )
        self.delete_full_rows()
        # Continuing of game
        self.time_counter += 1
        pass

    # Function checks if new shapes should be added
    #    and possible adds it
    def add_shape(self):

        # Checking if shape should be added
        if self.active_shape is None or not self.active_shape.is_active:
            self.time_counter = 0

            # Generates first blocks random X coordinate

            temp_x = random.randint(1, 6)

            # Getting random shape

            temp_shape = random.randint(0, 6)

            # Getting random color

            temp_color = random.randint(0, 6)

            # Generating blocks for new shape
            #    setting their is_active value as False
            #    because when these blocks are moving
            #    they can overlap for a moment and
            #    therefore stop moving ( because they
            #    hit an 'obstacle' )

            block_one = Block(temp_x + 3, 0 + 3, self.colors[temp_color])
            block_one.is_active = False

            block_two = Block(temp_x + 3, 0 + 3, self.colors[temp_color])
            block_two.is_active = False

            block_three = Block(temp_x + 3, 0 + 3, self.colors[temp_color])
            block_three.is_active = False

            block_four = Block(temp_x + 3, 0 + 3, self.colors[temp_color])
            block_four.is_active = False

            # Creating a shape made from prepared blocks

            self.active_shape = Shape(block_one, block_two, block_three, block_four, temp_shape)

            # Adding blocks to block list

            self.blocks.append(block_one)
            self.blocks.append(block_two)
            self.blocks.append(block_three)
            self.blocks.append(block_four)

            # Moving blocks to proper positions

            self.active_shape.rotate(self.shape_types, False)

            # Moving shape if needed

            for i in range(3):
                if not self.is_shape_ok(self.active_shape, False, self.grid):
                    self.active_shape.move_shape(0, 1)

            # If there is no place for new block, game ends

            if not self.is_shape_ok(self.active_shape, False, self.grid):
                self.running = False

    # Function checks if game is over
    def is_game_over(self):
        if not self.is_shape_ok(self.active_shape, False, self.grid):
            print("Game over!")
            self.get_name()
            self.running = False
            self.load_scores()
            self.scores[self.name] = self.points
            self.sort_scores()
            self.save_scores()

    # Function checks if active shape should be moved
    #    and moves it
    def move_active_shape(self, speed=200):

        # Checking if it should be moved

        if self.time_counter % speed == 0:

            # Moving shape

            self.active_shape.move_shape(0, 1)

            # Checking if moving was possible
            #    if it wasn't it means that shape should be blocked
            #    and new one should be added

            if not self.is_shape_ok(self.active_shape, False, self.grid):

                # Canceling last move

                self.active_shape.move_shape(0, -1)

                # Setting shapes block as non active and non moving

                self.active_shape.block_one.is_active = False
                self.active_shape.block_two.is_active = False
                self.active_shape.block_three.is_active = False
                self.active_shape.block_four.is_active = False

                self.active_shape.block_one.is_moving = False
                self.active_shape.block_two.is_moving = False
                self.active_shape.block_three.is_moving = False
                self.active_shape.block_four.is_moving = False

                # Resetting timer so new shape can be added

                self.time_counter = 5999

                # Setting shape as non active

                self.active_shape.is_active = False

    # Function checks if there are any full rows
    #    and deletes them
    def delete_full_rows(self):

        self.multiplier = 0

        # Function checks for every row check

        for row in range(self.rows):
            is_row_full = True
            temp_row_index = row

            # If there are any empty places for blocks

            for column in range(self.columns):
                if self.grid[row + 3][column + 3] == 0:
                    is_row_full = False

            # If any row doesnt have any blank spaces
            #    we search for blocks that are in this row
            #    ( have Y coordinate equal to row index + 3 ),
            #    3 is a correction
            #    and for every block from that row
            #    the block is set as nonactive, not alive and not moving

            if is_row_full:

                # Player gets extra points later
                self.multiplier += 1

                for block in self.blocks:
                    if block.y == temp_row_index + 3:
                        block.is_active = False
                        block.is_alive = False
                        block.is_moving = False
                # Then "dead" blocks are removed

                self.delete_dead_blocks()

                # Grids update

                self.update_grid()

                # Pushing down blocks

                self.correct_map(temp_row_index)

                # Adding points

                self.points += 100 * 2 ** self.multiplier

                self.my_string = "Score: " + str(self.points)

    # Function that is used after deleting full rows
    #    it removes dead blocks from blocks list
    def delete_dead_blocks(self):
        for block in self.blocks:
            if not block.is_alive:
                self.blocks.remove(block)

    # Function that is used after deleting full rows
    #    it pushes all blocks down if possible
    def correct_map(self, row):
        for block in self.blocks:
            if block.y < row + 3:
                block.y += 1

    # -------------------------------------------------------------------- #
    # ------------------------- helper functions ------------------------- #
    # -------------------------------------------------------------------- #

    # function adds selected image to given layout
    def add_image(self, layout, image):
        pix_map = QPixmap(image)
        label = QLabel()
        label.setPixmap(pix_map)
        layout.addWidget(label)

    # helper function setting buttons attributes
    def init_buttons(self, layout):

        # general size

        button_height = 200
        button_width = 470

        # size of actual game

        content_height = 100
        content_width = 350

        # start button

        self.start.clicked.connect(self.start_clicked)
        self.start.setGeometry(button_width, button_height, content_width, content_height)
        self.start.setIcon(QtGui.QIcon("button_icon.png"))

        # rules button

        self.rules.clicked.connect(self.rules_clicked)
        self.rules.setGeometry(button_width, button_height, content_width, content_height)
        self.rules.setIcon(QtGui.QIcon("button_icon.png"))

        # high scores button

        self.high_scores.clicked.connect(self.high_scores_clicked)
        self.high_scores.setGeometry(button_width, button_height, content_width, content_height)
        self.high_scores.setIcon(QtGui.QIcon("button_icon.png"))

        # author button

        self.author.clicked.connect(self.author_clicked)
        self.author.setGeometry(button_width, button_height, content_width, content_height)
        self.author.setIcon(QtGui.QIcon("button_icon.png"))

        # quit button

        self.end.clicked.connect(self.end_clicked)
        self.end.setGeometry(button_width, button_height, content_width, content_height)
        self.end.setIcon(QtGui.QIcon("button_icon.png"))

        # adding ready buttons to given layout

        layout.addWidget(self.start)
        layout.addWidget(self.rules)
        layout.addWidget(self.high_scores)
        layout.addWidget(self.author)
        layout.addWidget(self.end)

    def save_scores(self):
        if self.scores:
            with open('scores.txt', 'w') as file:
                file.write(json.dumps(self.scores))

    def load_scores(self):
        if not os.stat("scores.txt").st_size == 0:
            file = open('scores.txt', 'r')
            self.scores = ast.literal_eval(file.read())

    def game_init(self):

        # Creating window

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Tetris')

        pygame.init()

        self.grid = self.create_grid()

        self.active_shape = None
        # Time managing variable
        self.time_counter = 5999
        self.blocks = []
        # All shapes are stored in this list
        self.shapes = []
        # Game grid
        self.grid = self.create_grid()
        # Players points
        self.points = 0
        # If multiple rows get deleted player gets more points
        self.multiplier = 0
        # Resetting text
        self.my_string = "Score: 0"

    # This helper function generates a logic grid that has size of
    #    20 x 10, but with extra 3 rows and columns in both directions for safety
    #
    #    0 0 0 | 0 0 0 0 0 0 0 0 0 0 | 0 0 0
    #                     :
    #                     :
    #    0 0 0 | 0 0 0 0 0 0 0 0 0 0 | 0 0 0
    # # # fun fact # # #
    #    rows and columns don't work here but work
    #    in next function :)))
    def create_grid(self):
        return [[0 for _ in range(16)] for _ in range(26)]

    # Helper function that draws map
    def draw_grid(self):
        for i in range(self.columns + 1):
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (i * self.block_size + self.top_left_x, self.top_left_y, 1, self.p_height))
        for i in range(self.rows + 1):
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (self.top_left_x, i * self.block_size + self.top_left_y, self.p_width, 1))

        self.text = self.font.render(self.my_string, True, (0, 255, 0), (0, 0, 128))
        self.screen.blit(self.text, self.text_rect)

    # Helper function updating logic grid
    #    if block is alive ( not deleted )
    #    and its not the moving one
    #    the place in grid where the block is
    #    is set as '1'
    def update_grid(self):
        for i in range(self.rows + 6):
            for j in range(self.columns + 6):
                self.grid[i][j] = 0
            for block in self.blocks:
                if block.is_alive and not block.is_moving:
                    self.grid[block.y][block.x] = 1

    # Helper function that asks for players name to save score
    def get_name(self):
        text, ok_pressed = QInputDialog.getText(self.window, "Get Players name", "Your name: ", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            self.name = text

    # Helper function that sorts scores
    def sort_scores(self):
        self.scores = {k: v for k, v in sorted(self.scores.items(), key=lambda item: item[1])}


def main():
    Menu()


if __name__ == "__main__":
    main()
