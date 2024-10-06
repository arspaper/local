import turtle as t


t.tracer(False)
k = 35
for i in range(2):
    t.right(120)
    t.forward(7 * k)
t.right(300)
for i in range(2):
    t.right(120)
    t.forward(7 * k)
t.penup()
for x in range(-30, 10):
    for y in range(-30, 10):
        t.goto(x * k, y * k)
        t.dot()
t.exitonclick()
