from turtle import Turtle, Screen

s = Screen()

s.setup(1200,500)

t =  Turtle()

def f():
    t.fd(100)
    t.left(60)


s.onkey(f,"Up")
s.listen()
s.mainloop()