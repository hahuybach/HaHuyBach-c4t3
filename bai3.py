import math
def ex3():
    x = [1,2,4,5,6]
    y = []
    z = []
    tongptz = 0
    for i in range(len(x)):
        y.append(math.pi / 2 - x[i])
        z.append(math.cos(x[i]) - math.sin(x[i]))
    for n in range(len(z)):
        tongptz = tongptz + z[n]
    return y,z,tongptz

