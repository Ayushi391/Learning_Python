from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_level()

    def current_level(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=("Arial", 25, "normal"))

    def update_level(self):
        self.level += 1
        self.clear()
        self.current_level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Arial", 25, "normal"))
 