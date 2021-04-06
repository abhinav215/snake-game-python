import random
import time
import turtle
import winsound


delay = 0.2
score = 0
try:
    with open("highscore.txt", "r") as f:
        high_score = f.read()
    high_score = int(high_score)
except:
    high_score = 0


#screen
scrn = turtle.Screen()
scrn.title("Snake Game @Abhinav_Bhatnagar")
scrn.bgcolor("green")
scrn.setup(width=600,height=600)
scrn.tracer(0)

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.penup()
snake.goto(0,0)
snake.shape("square")
snake.color("white")
#snake.shapesize(strech_width=20,strech_length=20)
snake.direction="stop"
move_speed = 20

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.goto(0,260)
pen.hideturtle()
pen.write("Score: {}   High-score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

#food
food = turtle.Turtle()
food.goto(0,0)
food.shape("circle")
food.color("red")
food.penup()
x=random.randint(-290,290)
y=random.randint(-290,290)
food.goto(x,y)

#body
segment = []


#functions

    
def dead():
    winsound.PlaySound("cry",winsound.SND_ASYNC)
    with open("highscore.txt", "w") as f:
        f.write(str(high_score))
    time.sleep(7)
##    for i in range(7):
##        for ele in segment:
##            ele.color("pink")
##            time.sleep(0.5)
##        for ele in segment:
##            ele.color("grey")
##            time.sleep(0.5)
    snake.goto(0,0)
    snake.direction="stop"
    for body_part in segment:
        body_part.goto(1000,1000)
    segment.clear()
    pen.clear()
    pen.write("Score: {}   High-score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    


def move():
    if snake.direction=="left":
        snake.setx(snake.xcor() - move_speed)
    if snake.direction=="right":
        snake.setx(snake.xcor() + move_speed)
    if snake.direction=="down":
        snake.sety(snake.ycor() - move_speed)
    if snake.direction=="up":
        snake.sety(snake.ycor() + move_speed)

def go_up():
    if snake.direction == "down":
        pass
    else:
        snake.direction = "up"
    
def go_down():
    if snake.direction == "up":
        pass
    else:
        snake.direction = "down"
    
def go_left():
    if snake.direction == "right":
        pass
    else:
        snake.direction = "left"
    
def go_right():
    if snake.direction == "left":
        pass
    else:
        snake.direction = "right"
    
#keyboard input
scrn.listen()
scrn.onkeypress(go_up, "Up")
scrn.onkeypress(go_up, "w")
scrn.onkeypress(go_up, "W")
scrn.onkeypress(go_down, "S")
scrn.onkeypress(go_down, "s")
scrn.onkeypress(go_down, "Down")
scrn.onkeypress(go_left, "a")
scrn.onkeypress(go_left, "A")
scrn.onkeypress(go_left, "Left")
scrn.onkeypress(go_right, "d")
scrn.onkeypress(go_right, "D")
scrn.onkeypress(go_right, "Right")

    
#main game loop
while True:
    scrn.update()
    #check for collision
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()<-290 or snake.ycor()>290:
        score=0
        delay = 0.2
        dead()


    #check for food
    if snake.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #score increment
        score = score + 10
        winsound.PlaySound("Eating",winsound.SND_ASYNC)
        if score > high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {}   High-score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

        #shorten the delay
        delay = delay * 0.9
        
        #add body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)
    
    #move segemnt
    for index in range(len(segment)-1, 0, -1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x,y)
    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x,y)
        
    move()

    #check for collision with body
    for body_part in segment:
        if body_part.distance(snake)<20:
            score=0
            delay = 0.2
            dead()
            
    
    time.sleep(delay)
    
scrn.mainloop()

    


#dead par color change thing

