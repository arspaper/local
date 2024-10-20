with open("26_17537.txt") as myFile:
    seats = myFile.readlines()
    N, M, K = seats[0].split()
    myMap = [0] * int(K)
    for i in range(int(K)):
        myMap[i] = [0] * int(M)
    for i in range(1, int(N)):
        a, b = seats[i].split()
        myMap[int(b) - 1][int(a) - 1] = 1
    print(myMap)
    # print(myMap)
