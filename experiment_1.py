import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

def experiemt_1(the_turtle):
    for i in range(5):
        the_turtle.forward(100)
        the_turtle.right(144)


experiemt_1(slowpoke)

turtle.mainloop()