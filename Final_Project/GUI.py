"""
    Garfield Maitland
    CS 5001
    11/28/2023
    Final Project - GUI.py
"""

import turtle
from Marble import Marble, MARBLE_RADIUS
from Point import Point
from random import randint
import os
from Game import MasterMind

offset = 5
WIDTH = 600 + offset
HEIGHT = 800 + offset


class Board:
    def __init__(self, position, width, height, game: MasterMind, leaderboard) -> None:
        self.colors = game.colors
        self.game = game
        self.position = position
        self.width = width
        self.height = height
        self.current_marble = 0
        self.guess_marbles = []
        self.scoring_pegs = []
        self.leaderboard = leaderboard
        self.draw()

        self.current_guess = 0
        self.guess_code = []

        # Initialize the Turtle for Guess Pointer
        self.turtle = turtle.Turtle()
        self.turtle.shapesize(2.2)
        self.turtle.pencolor("red")
        self.turtle.pu()
        self.turtle.speed(0)  # set to fastest drawing

    def draw_guess(self):
        self.turtle.goto(self.guess_marbles[0].position.x - 20, self.guess_marbles[0].position.y + MARBLE_RADIUS)

    def add_marble(self, color):
        self.guess_marbles[self.current_guess * 4 + self.current_marble].set_color(color)
        self.guess_marbles[self.current_guess * 4 + self.current_marble].draw()
        self.current_marble += 1
        self.guess_code.append(color)

    def clear_guess(self):
        for i in range(self.current_guess * 4, self.current_guess * 4 + 4):
            self.guess_marbles[i].draw_empty()
        self.current_marble = 0
        self.guess_code = []

    def guess(self):
        # self.turtle.goto(self.guess_marbles[self.current_guess*4].position.x-20,self.guess_marbles[0].position.y+MARBLE_RADIUS)
        if self.current_marble == 4:
            self.current_guess += 1
            self.current_marble = 0
            feedback = self.game.add_guess(self.guess_code)
            self.update_scoring_pegs(feedback)
            if self.game.get_game_state() == "playing":
                self.guess_code = []
                self.turtle.goto(self.guess_marbles[self.current_guess * 4].position.x - 20,
                                 self.guess_marbles[self.current_guess * 4].position.y + MARBLE_RADIUS)
            elif self.game.get_game_state() == "won":
                self.won()
            elif self.game.get_game_state() == "lost":
                self.lost()
            return self.game.get_game_state()

    def won(self):
        self.leaderboard.add_score(self.game.guess_count)
        Popup("Images/winner.gif")
        turtle.ontimer(turtle.bye, 2000)

    def lost(self):
        Popup("Images/Lose.gif")
        turtle.ontimer(self.show_code, 2000)

    def show_code(self):
        code = self.game.get_secret_code()
        turtle.textinput("Code", ' '.join(code))
        turtle.ontimer(turtle.bye, 500)

    def update_scoring_pegs(self, feedback):
        bulls = feedback["Bulls"]
        cows = feedback["Cows"]
        a = 0
        for i in range(bulls):
            self.scoring_pegs[(self.current_guess - 1) * 4 + a].set_color("black")
            self.scoring_pegs[(self.current_guess - 1) * 4 + a].draw()
            a += 1
        for i in range(cows):
            self.scoring_pegs[(self.current_guess - 1) * 4 + a].set_color("red")
            self.scoring_pegs[(self.current_guess - 1) * 4 + a].draw()
            a += 1

    def draw(self) -> None:
        Frame(self.position, self.width, self.height)
        for row in range(0, 10):
            for column in range(0, 4):
                x = 40 + self.position.x + MARBLE_RADIUS + column * (MARBLE_RADIUS * 3)
                y = (self.position.y + self.height - row * self.height / 11) - MARBLE_RADIUS * 4
                marble = Marble(Point(x, y), "black")
                marble.draw_empty()
                self.guess_marbles.append(marble)
            for _ in range(0, 4):
                x = self.position.x + self.width - self.width / 4 + ((_ + 1) % 2) * -20
                _y = 0
                if _ >= 2:
                    _y = 20
                y = self.position.y + self.height - row * self.height / 11 - MARBLE_RADIUS * 3 - _y
                marble = Marble(Point(x, y), "black", size=4)
                marble.draw_empty()
                self.scoring_pegs.append(marble)


class Leaderboard:
    def __init__(self, position, width, height) -> None:
        self.playername = turtle.textinput("Name", "Enter your name:")
        if self.playername == None or self.playername == "":
            self.playername = "Unknown"
        self.position = position
        self.width = width
        self.height = height
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)  # set to fastest drawing
        self.turtle.color("blue")
        self.turtle.up()

        self.leaders = []
        self.load_all_leaders()
        self.draw()

    def load_all_leaders(self):
        if os.path.exists("leaderboard.txt"):
            with open("leaderboard.txt", "r") as f:
                lines = f.read().split("\n")

                for line in lines:
                    _ = line.split(":")
                    if len(_) == 2:
                        self.leaders.append((_[0], _[1]))


        else:
            with open("leaderboard.txt", "w") as f:
                f.write("")
        self.leaders = sorted(self.leaders, key=lambda x: int(x[0]))[:10]

    def add_score(self, guess_count):
        self.leaders.append((guess_count, self.playername))
        self.leaders = sorted(self.leaders, key=lambda x: int(x[0]))[:10]
        with open("leaderboard.txt", "w") as f:
            for leader in self.leaders:
                f.write(str(leader[0]) + ":" + leader[1] + "\n")

    def draw(self) -> None:

        Frame(self.position, self.width, self.height, "blue")
        self.turtle.goto(self.position.x + 10, self.position.y + self.height - 40)
        self.turtle.write("Leaders:", font=("Arial", 20, "normal"))
        for i in range(len(self.leaders)):
            self.turtle.goto(self.position.x + 10, self.position.y + self.height - 90 - (i * 30))
            self.turtle.write(f"{self.leaders[i][0]}:{self.leaders[i][1]}", font=("Arial", 20, "normal"))


class User_Panel:
    def __init__(self, board, position, width, height, window) -> None:
        self.board = board
        self.position = position
        self.width = width
        self.height = height
        self.colors = board.colors
        self.marbles = []
        self.disabled_colors = []
        self.window = window
        self.draw()

    def enter_code(self):
        if self.window.screen_lock == False:
            self.window.screen_lock = True
            if len(self.disabled_colors) == 4:
                state = self.board.guess()
                if state == "playing":
                    for i, marble in enumerate(self.marbles):
                        marble.draw()
                    self.disabled_colors = []
            self.window.screen_lock = False

    def clear_code(self):
        if self.window.screen_lock == False:
            self.window.screen_lock = True
            self.board.clear_guess()
            for marble in self.marbles:
                marble.draw()
            self.disabled_colors = []
            self.window.screen_lock = False

    def quit(self):
        if self.window.screen_lock == False:
            self.window.screen_lock = True
            Popup("Images/quitmsg.gif")
            turtle.ontimer(turtle.bye, 1000)
        # turtle.bye()

    def on_click(self, x, y):
        if len(self.disabled_colors) < 4:
            for i, marble in enumerate(self.marbles):
                if marble.clicked_in_region(x, y) and not marble.color in self.disabled_colors:
                    marble.draw_empty()
                    self.board.add_marble(marble.color)
                    self.disabled_colors.append(marble.color)
                    break

    def draw(self):
        Frame(self.position, self.width, self.height)
        self.enter_button = ImageButton("Images/checkbutton.gif", Point(self.width / 2 + 40, self.height / 2), 200, 200,
                                        self.enter_code)
        self.reset_button = ImageButton("Images/xbutton.gif", Point(self.width / 2 + 120, self.height / 2), 200, 200,
                                        self.clear_code)
        self.quit_button = ImageButton("Images/quit.gif", Point(self.width / 2 + 220, self.height / 2), 200, 200,
                                       self.quit, repeat=False)
        for i in range(len(self.colors)):
            marble = Marble(Point(30 + self.position.x + MARBLE_RADIUS + i * (MARBLE_RADIUS * 3),
                                  self.position.y + self.height / 2), self.colors[i])
            marble.draw()
            self.marbles.append(marble)


class ImageButton:
    def __init__(self, image: str, position: Point, width: int, height: int, action=print, repeat=True) -> None:
        self.position = position
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(self.position.x, self.position.y)
        self.turtle.shape(image)
        self.action = action
        self.repeat = repeat
        self.turtle.onclick(self.execute)

    def execute(self, x, y):
        self.turtle.onclick(None)
        self.action()
        if self.repeat:
            self.turtle.onclick(self.execute)


class Frame:
    def __init__(self, position, width, height, color="black") -> None:
        self.position = position
        self.width = width
        self.height = height
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(7)
        self.pen.color(color)
        self.draw()

    def draw(self):
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.goto(self.position.x + self.width, self.position.y)
        self.pen.goto(self.position.x + self.width, self.position.y + self.height)
        self.pen.goto(self.position.x, self.position.y + self.height)
        self.pen.goto(self.position.x, self.position.y)
        self.pen.up()


class Popup:
    def __init__(self, image: str):
        self.position = Point(WIDTH / 2, HEIGHT / 2)
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(self.position.x, self.position.y)
        self.turtle.shape(image)


class MasterMind_UI:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.setup(width=WIDTH, height=HEIGHT)
        self.window.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        self.window.addshape("Images/checkbutton.gif")
        self.window.addshape("Images/xbutton.gif")
        self.window.addshape("Images/quit.gif")
        self.window.addshape("Images/winner.gif")
        self.window.addshape("Images/Lose.gif")
        self.window.addshape("Images/quitmsg.gif")
        self.screen_lock = True

    def on_click(self, x, y):
        if self.screen_lock == False:
            self.window.onscreenclick(None)
            self.user_panel.on_click(x, y)
            self.window.onscreenclick(self.on_click)

    def start_game(self, game):
        self.game = game

        leaderboard = Leaderboard(position=Point(410, 160), width=190, height=640)
        board = Board(position=Point(0, 160), width=400, height=640, game=game, leaderboard=leaderboard)
        self.user_panel = User_Panel(board, position=Point(0, 0), width=600, height=150, window=self)

        self.window.onscreenclick(self.on_click)
        self.screen_lock = False

        self.window.mainloop()
