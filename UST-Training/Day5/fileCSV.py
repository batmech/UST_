import csv
from random import choice

with open('Employe.csv', 'w', newline='') as fp:
    while True:
        pid = int(input('Enter PID: '))
        name = input('Enter name: ')
        occupation = input('Enter occupation: ')
        write = csv.writer(fp)
        write.writerow([pid, name, occupation])
        choice = input('Do you want to continue? (y/n)').lower()
        if choice[0] == 'n': break