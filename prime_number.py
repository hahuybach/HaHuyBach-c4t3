num = int(input("so cua m la gi?"))
chiahet = 0
if num == 1:
    print("1 is a prime number")
    exit()
for i in range(1,num+1):
    if num % i == 0:
        chiahet += 1

if chiahet == 2:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

