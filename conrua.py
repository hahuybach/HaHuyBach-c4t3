from turtle import*
shape("turtle")

x = 10
for i in range(50):
    for i in range(4):
        forward(x)
        left(90)
    right(30)
    x=x+10

mainloop()