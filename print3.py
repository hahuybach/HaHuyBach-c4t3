number = []
x = 1
for _ in range(6):
    number.append(x)
    x -= 1
    number.append(x)
    x += 1
print(*number)
