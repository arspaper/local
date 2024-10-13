def func(line):
    while "52" in line or "1122" in line or "2222" in line:
        if "52" in line:
            line = line.replace("52", "11", 1)
        if "2222" in line:
            line = line.replace("2222", "5", 1)
        if "1122" in line:
            line = line.replace("1122", "25", 1)
    return sum(list(map(int, list(line))))



for n in range(4, 10000):
    myLine = "5" + "2" * n
    result = func(myLine)
    if result == 64:
        print(n)
        break