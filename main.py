# laba_7_last

import csv
from numpy import random
import os


def Show(separator=',', order='top', rows=5):
    rowcount = -1
    for row in open("Titanic.csv"):
        rowcount += 1

    if rows > rowcount:
        print("Not enough rows in csv file")
        return

    f = open("Titanic.csv")
    csv_f = csv.reader(f, delimiter=separator)

    if order == 'top':
        for i, row in enumerate(csv_f):
            print('{:<12} {:<10} {:<10} {:<55} {:<10} {:<10} {:<10} {:<10} {:<20} {:<15} {:<15} {:<10} '.format(*row))
            if i >= rows:
                break

    if order == 'bottom':
        for i, row in enumerate(csv_f):
            if i >= (rowcount - rows) or i == 0:
                print(
                    '{:<12} {:<10} {:<10} {:<55} {:<10} {:<10} {:<10} {:<10} {:<20} {:<15} {:<15} {:<10} '.format(*row))

    if order == 'random':
        random_array_numbers = random.randint(1, rowcount, size=(rows))
        for i, row in enumerate(csv_f):
            if i in random_array_numbers or i == 0:
                print(
                    '{:<12} {:<10} {:<10} {:<55} {:<10} {:<10} {:<10} {:<10} {:<20} {:<15} {:<15} {:<10} '.format(*row))


def Info():
    rowcount = -1
    columncount = 0
    f = open("Titanic.csv")
    csv_f = csv.reader(f)

    for i, row in enumerate(csv_f):
        if i == 0:
            columncount = len(row)
        rowcount += 1
    print(str(rowcount) + "x" + str(columncount))

    f = open("Titanic.csv")
    csv_f = csv.reader(f)
    numbers = [0] * columncount
    column_names = []
    data_types = []
    line_count = 0
    for row in csv_f:
        if line_count != 0:
            for i in range(columncount):
                if row[i] != '':
                    numbers[i] += 1
                if line_count == 1:
                    for j in range(columncount):
                        data_types.append(type(row[j]))
                        line_count += 1
        else:
            for i in range(columncount):
                column_names.append(row[i])
            line_count += 1

    for i in range(columncount):
        print(column_names[i], numbers[i], data_types[i])


def DelNaN():
    lines = list()
    with open('Titanic.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == '':
                    lines.remove(row)
                    break
    with open('Titanic_output.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


def MakeDS():
    rowcount = -1
    for row in open("Titanic.csv"):
        rowcount += 1

    os.mkdir("workdata")
    os.chdir("workdata")
    os.mkdir("Learning")
    os.mkdir("Testing")
    train_lines = list()
    test_lines = list()
    rows_in_train = int(rowcount * 0.7)
    random_rows = x = random.randint(1, rowcount, size=rows_in_train)
    with open('Titanic.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for i, row in enumerate(reader):
            if i in random_rows or i == 0:
                train_lines.append(row)
            if i not in random_rows or i == 0:
                test_lines.append(row)

    with open('train.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(train_lines)

    with open('test.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(test_lines)

    os.replace("train.csv", "Learning/train.csv")
    os.replace("test.csv", "Testing/test.scv")


if __name__ == '__main__':
     Show()
    # Info()
    #DelNaN()
    #MakeDS()
