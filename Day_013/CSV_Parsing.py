import csv

with open('data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Harry', 'Gryffindor'])
    w.writerow(['Hermione', 'Gryffindor'])
    w.writerow(['Draco', 'Slytherin'])

with open('data.csv', 'r') as f:
    for r in csv.DictReader(f, fieldnames=['Name', 'House']):
        print(r)