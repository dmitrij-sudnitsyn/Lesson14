# try:
#     file = open('todo2.txt', mode='a+', encoding='utf')
#     file.write("qwerty\t")
#     file.write("asd")
#     file.writelines(['\nqwerty','\nasd'])
#     # file.readable()
#     # print(file.readline())
#     file.seek(50)
#     file.write("asd")
#     st = file.read()
#     print(st)
# except Exception as e:
#     print(e.args)
# finally:
#     file.close()
import csv

# with open('todo2.txt', mode='r', encoding='utf') as f1, open('todo4.txt', mode='a', encoding='utf') as f2:
#     f2.write(f1.read())

group = [
    ['Дьомшина Анастасія Миколаївна', 329],
    ['Войтенко Артем Анатолійович', 278],
    ['Судніцин Дмитро Вікторович', 267]
]

student = ['Гончаров Роман Костянтинович', 242]

with open('table.csv', mode='w', encoding='utf') as file:
    writer = csv.writer(file, dialect='excel', lineterminator="\n")
    writer.writerows(group)
    writer.writerow(student)

group2 = []
with open('table.csv', mode='r', encoding='utf') as file:
    reader = csv.reader(file)
    for el in reader:
        if el != []:
            group2.append(el)
            print(el[1])

print(group2)

group = [
    {"fio":'Дьомшина Анастасія Миколаївна', "rate":329},
    {"fio":'Войтенко Артем Анатолійович', "rate":278},
    {"fio":'Судніцин Дмитро Вікторович', "rate":267}
]

with open('table.csv', mode='w', encoding='utf') as file:
    writer = csv.DictWriter(file, group[0], lineterminator="\n")
    writer.writeheader()
    writer.writerows(group)

with open('table.csv', mode='r', encoding='utf') as file:
    reader = csv.DictReader(file, group[0])
    for el in reader:
        print(el["rate"])

#.dll


   

