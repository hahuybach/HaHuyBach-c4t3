menu = ["player","enemy1"]
print(menu)
tendich = input(" Quan dich ten la gi? ").lower()
menu.append(tendich)
print(menu)
hoi = input(" Shoot or Spawn").lower()


if hoi.lower() == "shoot":
    menu.append("bullet")

elif  hoi.lower() == "spawn":
    menu.append("enemy")
print(menu)