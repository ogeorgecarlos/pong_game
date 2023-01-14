from turtle import Screen
from padle import padle_right, padle_left

width = 800
height = 600
color = 'black'
title = 'Pong'


class Myscreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(width=width, height=height)
        self.screen.bgcolor(color)
        self.screen.title(title)
        self.screen.listen()

    def exitonclick(self):
        self.screen.exitonclick()

    def moviment(self):
        self.screen.onkeypress(padle_right.move_up, "Up")
        self.screen.onkeypress(padle_right.move_down, "Down")
        self.screen.onkeypress(padle_left.move_up, "w")
        self.screen.onkeypress(padle_left.move_down, "s")

    def update(self):
        self.screen.update()
