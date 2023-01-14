from screen import Myscreen
from padle import padle_right,  padle_left, dashed_line, pong, left_score, right_score
from time import sleep


# import screen of the pong game and defitions
screen = Myscreen()
screen.moviment()

# import all objects created with a turtle
padle_right.right()
padle_left.left()
dashed_line.dashed()
pong.pong()
left_score.left_score()
right_score.right_score()

while True:
    sleep(pong.vel)
    screen.update()
    pong.pong_move()
    # detect colision with border up and down
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.pong_bounce_y()
    # detect colision with right padle
    if pong.xcor() > 350 and pong.distance(padle_right) < 50:
        pong.pong_bounce_x()
    # if the pong go out the border sum 1 point to score.
    elif pong.xcor() > 370:
        left_score.plus_left_score()
        left_score.left_score()
        pong.home()
    # detect colision with left padle
    if pong.xcor() < -350 and pong.distance(padle_left) < 50:
        pong.pong_bounce_x()
    # if the pong go out the border sum 1 point to score.
    elif pong.xcor() < - 385:
        right_score.plus_right_score()
        right_score.right_score()
        pong.home()


screen.exitonclick()
