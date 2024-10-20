
# import pandas as pd
import csv


# df = pd.read_excel('09.xlsx')
# df.to_csv('09.csv', index=False)

with open('09.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in range(6):
