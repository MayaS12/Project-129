import pandas as pd
import csv

file_1 = 'brightest_stars.csv'
file_2 = 'unit_converted_dwarf_stars.csv'

d1 = []
d2 = []

with open(file_1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d1.append(i)

with open(file_2, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]
t_d1 = d1[1:]
t_d2 = d2[1:]

h = h1+h2
t_d = []
for i in t_d1:
    t_d.append(i)
for g in t_d2:
    t_d.append(g)

with open("total_stars.csv", 'w', encoding='utf8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(t_d)

df = pd.read_csv("total_stars.csv")
print(df.tail(8))