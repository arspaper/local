def func(line):
    while "1111" in line:
        line = line.replace("1111", "22", 1)
        line = line.replace("222", "1", 1)
    return line.count("1")


minOnes = 100000
minN = 100000
for n in range(200, 10000):
    myLine = "1" * n
    result = func(myLine)
    if result < minOnes:
        minOnes = result
        minN = n

print(minN)