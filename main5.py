f = open('1_9.txt')
count = 0
for s in f:
    m=[int (x) for x in s.split()]
    m.sort()
    if len(set(m))==5 and 2*(m[0]+m[-1]) <= sum(m) - (m[0]+m[-1]):
        count += 1
print(count)