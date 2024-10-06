import pandas as pd
import csv


df = pd.read_excel('99.xlsx')
df.to_csv('99.csv', index=False)


f = open('99.csv')
k = 0
p = []
for s in f:

    a = sorted(list(map(int,s.split(','))))
    for i in range(len(a)-1):
        if a[i]==a[i+1] and len(set(a))==5:
            p.append(a[i])
            if (a[i])*2 < (sum(a)-((a[i])*2))/4:
                k += 1
print(k)