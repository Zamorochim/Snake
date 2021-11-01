from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard import Scoreboard
import time

game_is_on = True
speed = 0.1
screen = Screen()
screen.bgcolor("gold")
screen.screensize(800, 800)
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(speed)

    # Detect collision with food.
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        speed *= 0.95

    # Detect collision with walls.
    if snake.head.xcor() > 450 or snake.head.xcor() < -460 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        speed = 0.1

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            speed = 0.1


screen.exitonclick()

