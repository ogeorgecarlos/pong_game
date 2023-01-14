from turtle import Turtle

padle_color = 'white'
padle_shape = 'square'
padle_pos_right = 370
padle_pos_left = -370
padle_pos_dashed = -370
pong_pos = 45
x_move = 10
y_move = 10
total_left_score = 0
total_right_score = 0


class Padle(Turtle):
    def __init__(self):
        '''Create a pattern config to padles'''
        super().__init__()
        self.shape(padle_shape)
        self.penup()
        self.shapesize(0.7, 4)
        self.color(padle_color)
        self.setx(0)
        self.vel = 0.05

    def right(self):
        '''Move the padle to the position right of the screen's border'''
        self.setx(padle_pos_right)
        self.setheading(90)

    def left(self):
        '''Move the padle to the position left of the screen's border'''
        self.setx(padle_pos_left)
        self.setheading(90)

    def dashed(self):
        '''To create the dased line in the centerof the screen'''
        self.sety(-280)
        self.pendown()
        self.hideturtle()
        self.pensize(width=5)
        self.setheading(90)
        for _ in range(20):
            self.fd(20)
            self.penup()
            self.fd(20)
            self.pendown()

    def pong(self):
        '''Create the pong object'''
        self.shape('square')
        self.shape('circle')
        self.shapesize(1, 1)
        self.setheading(pong_pos)

    def pong_move(self):
        '''Set the pong moviment'''
        new_y = self.ycor() + y_move
        new_x = self.xcor() + x_move
        self.goto(new_x, new_y)

    def pong_bounce_y(self):
        '''Update the pong moviment when this one touch the up or down border'''
        global y_move
        y_move *= -1

    def pong_bounce_x(self):
        '''Update the pong moviment when this colid with a padle'''
        global x_move
        x_move *= -1

    def left_score(self):
        '''create a new object to show the left score'''
        self.hideturtle()
        self.setposition(x=-100, y=250)
        self.pencolor('white')
        self.clear()
        self.write(total_left_score, align='center', font=('Arial', 30, 'normal'))

    def plus_left_score(self):
        '''A function to update the left score'''
        global total_left_score
        total_left_score += 1

    def right_score(self):
        '''create a new object to show the left score'''
        self.hideturtle()
        self.setposition(x=100, y=250)
        self.pencolor('white')
        self.clear()
        self.write(total_right_score, align='center', font=('Arial', 30, 'normal'))

    def plus_right_score(self):
        '''A function to update the right score'''
        global total_right_score
        total_right_score += 1

    def move_up(self):
        '''Create a moviment to the padle (up)'''
        self.forward(20)

    def move_down(self):
        '''Create a moviment to the padle (down)'''
        self.backward(20)


# all objects created with turtle
padle_right = Padle()
padle_left = Padle()
dashed_line = Padle()
pong = Padle()
left_score = Padle()
right_score = Padle()
