from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# TODO: 1. Create Snake
snake = Snake()
# TODO : 4. Create Food
food = Food()
# TODO: 6. Make ScoreBoard
scoreboard = ScoreBoard()

# TODO: 3. Control the Snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO: 2. Moves Snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: 5. Detect Collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        # TODO: 8. Extending snake tail
        snake.extend()

    # TODO: 7. Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # TODO: 9. Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 12:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
