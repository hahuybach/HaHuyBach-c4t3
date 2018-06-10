x = [1,6,8,1,2,1,5,6]
so_m_chon = int(input("m chon so nao?"))
count = 0
for i in x:
    if i == so_m_chon:
        count+= 1
print(so_m_chon,"appears",count,"times")
