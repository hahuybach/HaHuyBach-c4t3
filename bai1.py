def manginra(x):
    z = 2

    mang = []
    k = -1
    for i in range(x):
        if i % 2 == 0:
            mang.append(z)
            z = z - 0.5
        else:
            mang.append(k)

    return mang


