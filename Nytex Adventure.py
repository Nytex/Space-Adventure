#Nytex Adventure
import turtle
import os
import math
import random
import winsound

winsound.PlaySound("adventure",winsound.SND_ASYNC)

#Setup the Screen
wn = turtle.Screen()
wn.bgcolor("black") #The background color
wn. title("Nytex Adventure") #The title of the Apps
wn.bgpic("ttest.gif")

#Register the shapes
turtle.register_shape("spaceship.gif")
turtle.register_shape("ufo.gif")
turtle.register_shape("ball.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('yellow')
border_pen.penup()
border_pen.setposition(-300,-300) #The position of the collumn
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(600) #这个是长度 The length of the border
    border_pen.lt(90) #这个格子的角度 The angle of between lines
border_pen.hideturtle()

#Set the Score to 0
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("gold")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("yellow")
player.shape("spaceship.gif") #可是triangle facing 右边
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90) #让triangle face 去上面

#Speed Variable 速度定义
playerspeed = 15
enemyspeed = 5 #Slow compare to player
bulletspeed = 30 #Fastest in game


#Choose number of Enemies
number_of_enemies = 5

enemies = []

for i in range(number_of_enemies):
      enemies.append(turtle.Turtle())

#Enemy properties
for enemy in enemies: 
      enemy.color("red")
      enemy.shape("ufo.gif")
      enemy.penup()
      enemy.speed(0)
      x = random.randint(-200, 200)
      y = random.randint(100, 250)
      enemy.setposition(x, y)


#Create Bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("ball.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#Bullet State
#Ready to fire

#Fire
bulletstate = 'ready'


#All the Function 全部Function
#Move to left
def move_left():
    x = player.xcor()
    x -= playerspeed #Ensure X doesn't move outside border
    if x < -280:
        x = -280
    player.setx(x)
    

#Move to Right
def move_right():
    x = player.xcor()
    x += playerspeed #Ensure X doesn't move outside border
    if x > 280:
        x = 280
    player.setx(x)
    
    
#Fire Bullet
def fire_bullet():
        global bulletstate #declare bulletstate as global
        if bulletstate =="ready":
            bulletstate = "fire" #Ensure bullet does'nt reset
            x = player.xcor()
            y = player.ycor() + 15
            bullet.setposition(x,y)
            bullet.showturtle()

#Collision 相撞
def isCollision(t1, t2):
      distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
      if distance < 15:
            return True
      else:
            return False
                           
                        


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:

    for enemy in enemies:
          x = enemy.xcor()
          x += enemyspeed
          enemy.setx(x)
          if enemy.xcor() > 280:
                #Enemy move right and return
                for e in enemies:
                      #Ensure only one Enemy reset
                      y = e.ycor()
                      y -= 30
                      e.sety(y)
                enemyspeed *= -1
        

          if enemy.xcor() < -280:
                #Enemy move left and return
                for e in enemies:
                      y = e.ycor()
                      y -= 30
                      e.sety(y)
                enemyspeed *= -1 #All enemy same speed change
                
          #Check for a collision between bullet and enemy
          if isCollision(bullet, enemy):
                bullet.hideturtle() #For bullet
                bulletstate= "ready"
                bullet.setposition(0, -400)

                x = random.randint(-200, 200)
                y = random.randint(150, 250)
                enemy.setposition(x, y)  #For Enemy
                #Update the score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear() #不然会在0 上面print 新score
                score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))
                

          if isCollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print ("Game Over")
                break
  



    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #But the bullet will be reset everytime you press so go above

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    
          


    


    
delay = raw_input("Press Enter to Finish")
