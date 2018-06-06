# food1 = "Egg"
# food2 = "Bun dau mam tom"
# food3 = "So huyet"
# food4 = "Rau xanh"
# food5 = "Pho"
# menu = []
# print(menu)
# print(type(menu))
# menu = ["trung"]
# print(menu)
menu = ["trung","rau","pho","com rang"]
# numbers = ["1.","2.","3."]
# no = 1
# # menu.append("bun dau")
# # print(*menu, sep=", ")
# # menu.insert(0, "so huyet")
# # print(*menu, sep=", ")
# for food in menu:
#     print(no,food, sep=".")
#     no = no + 1
# print(menu)
# menu.pop()
# menu.remove("pho")

# print(menu)
# i = int(input("enter position: "))
# new_food = input("Enter replacing food: ?")
#
# menu[i] = new_food
# print(*menu, sep=", ")
for index, food in enumerate(menu):
    print(index + 1, food, sep=". ")