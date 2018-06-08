action = input("welcome to our shop, what do you want (c,r,u,d) ? ").lower()

ouritems = ["Tshirt","sweater"]

if action == "r":
    print("our items : ")
    print(*ouritems,sep = ",")

elif action == "c":
    newitems = input("Enter new items :")
    ouritems.append(newitems)
    print("our items : ")
    print(*ouritems, sep = ",")

elif action == "u":
    pos = int(input("Enter new position :"))
    newitems = input("Enter new items :")
    ouritems.insert(pos,newitems)
    print("our items : ")
    print(*ouritems, sep=",")

elif action == "d":
    deletepos = int(input("Delete position :"))
    ouritems.pop(deletepos-1)
    print("our items : ")
    print(*ouritems, sep=",")
