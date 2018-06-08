n = int(input("nhap so n"))
x = 1
number = []


for _ in range((n//2)+1):
    number.append(x)
    x -= 1
    number.append(x)
    x += 1
if n % 2 != 0:
    number.pop()

print(*number)