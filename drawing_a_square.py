import turtle
bob = turtle.Turtle()
print(bob)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)
bob.hideturtle()
turtle.mainloop()

turtle.done()
