import json
with open('some.json') as r:
    data = json.load(r)
    print(data['name'])

f = open('some.csv', 'r')

for line in f:
    print(line)
f.close()

with open('some.csv') as f:
    print(f.read())

import csv
with open('some.csv') as f:
    animals = csv.reader(f)
    for row in animals:
        if row[-1] == 'True':
            print('{0} ok {1}'.format(row[0], row[1]))
