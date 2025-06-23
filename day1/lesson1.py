from turtle import *


#we want to paint house
shape("turtle")
width(7)

color("blue")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square



forward(70)
color("brown")
begin_fill()
left(90)
forward(100)
right(90) 
forward(60)
right(90)
forward(100)
end_fill()




penup()
goto(200, 200)
pendown()
color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

penup()
goto(140, 140)
pendown()
color("white")
begin_fill()
left(120)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()



penup()
goto(20, 140)
pendown()
color("white")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()


penup()
goto(-999, 0)
pendown()
color("green")
begin_fill()
speed(999)
forward(9999)
left(90)
forward(9999)
left(90)
forward(9999)
left(90)
forward(9999)
left(90)
forward(9999)
end_fill()


penup()
goto(-600, 350)
pendown()
color("yellow")
begin_fill()
circle(40)
end_fill()


exitonclick()