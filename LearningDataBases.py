import csv

def learning():
    with open('a.csv', newline='', encoding='UTF-8') as file:
        reader = csv.reader(file)
    next(reader)
    print(reader[0])

learning()