from turtle import Turtle
#creating paddle
class Paddle(Turtle): 

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor,y_cor)

    def go_up(self):
        new_up = self.ycor() + 20
        self.goto(self.xcor(), new_up)

    def go_down(self):
        new_down = self.ycor() - 20
        self.goto(self.xcor(), new_down)