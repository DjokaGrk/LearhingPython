import turtle

screen = turtle.Screen()
screen.title("States Game")
screen.setup(width=740, height=1024)
image = "EuropePrintText-740x1024.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click(x, y):
    print(f"Mouse clicked at: ({x}, {y})")


turtle.onscreenclick(get_mouse_click)
turtle.mainloop()


screen.exitonclick()
