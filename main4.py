with open("24_6029.txt", mode='r') as myFile:
    line = myFile.readline()
    highestStreak = 0
    previousSymbol = line[0] # F
    currentStreak = 1
    for i in range(1, len(line)):
        currentSymbol = line[i]
        if currentSymbol == 'E':
            if previousSymbol == 'F':
                currentStreak += 1
            else:
                highestStreak = max(highestStreak, currentStreak)
                currentStreak = 1
        elif currentSymbol == 'F':
            if previousSymbol == 'E':
                currentStreak += 1
            else:
                highestStreak = max(highestStreak, currentStreak)
                currentStreak = 1
        else:
            highestStreak = max(highestStreak, currentStreak)
            currentStreak = 1
        previousSymbol = currentSymbol
    print(highestStreak)
