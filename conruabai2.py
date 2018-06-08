from turtle import*
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
z = -4
n = 3
for i in range(4):
    pencolor(colors[z])
    for i in range(n):
        forward(100)
        left(360/n)
    n = n + 1
    z = z +1
mainloop()
