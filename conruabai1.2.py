from turtle import*
color=["blue","red"]
z=-2
n=3
for i in range(4):
    pencolor(color[z])
    for i in range(n):
        forward(100)
        left(360/n)
    n = n + 1
    z = z +1
mainloop()
