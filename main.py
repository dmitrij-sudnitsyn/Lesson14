# Создать программу в которой пользователь вводит 2 числа и ему возвращается результат деления этих чисел, после вопрос хочет ли он повторить.
# При выполнении программы записывать ее выполнение в лог файл. Если не было исключений записать лог с типом Info с сообщением вводимых чисел и результата.
# Если возникло исключение - с типом Error и сообщением какое исключение было вызвано.
# Когда пользователь на вопрос хочет ли он повторить ответит "нет" прочитать файл логов и вывести на экран кол-во с типом Info и кол-во с типом Error
import datetime
print("Hello word")
print("Данная программа производить деление одного деления на другое и выводить значение в лог файл")

with open("lesson.log", mode="a", encoding="utf") as file:
 i=''
 s='y'
 str1='True'
 while s=='y':
  while str1=='True':   
   try:
    a=int(input("Введите первое число= "))  
    break
    str1='False'
   except ValueError:
    file.writelines(f'Error при вводе первого числа вы ввели не число {datetime.datetime.now()}\n')
    print(f'Error при вводе первого числа вы ввели не число {datetime.datetime.now()}')
    print("Попробуйте еще раз.")
   
  while str1=='True':   
   try:
    b=int(input("Введите второе число= "))  
    break
    str1='False'
   except ValueError:
    print(f'Error при вводе второго числа вы ввели не число {datetime.datetime.now()}')
    file.writelines(f'Error при вводе второго числа вы ввели не число {datetime.datetime.now()}\n')
    print("Попробуйте еще раз.")
  try:
   c=a/b
   print(f"Результат деления {a}/{b}={c} {datetime.datetime.now()}")
   file.writelines(f'Info Результат деления {a} / {b} = {c} {datetime.datetime.now()}\n')
  except ZeroDivisionError:
   print(f'Error деление  на 0 {a}/{b} не допустимо {datetime.datetime.now()}')   
   file.writelines(f'Error деление  на 0 {a} / {b} не допустимо {datetime.datetime.now()}\n')

  print("Продолжим деление?")
  print("Введите Да или Y если хотите повторить")
  print("Введите Нет или n если хотите закончить")
  i=input("Продолжить? ")
  if i=="нет" or i=="n":
   s='n'  

# with open("lesson.log", mode="a", encoding="utf") as file:
intError=0
intInfo=0
list_str=[]
with open("lesson.log", mode="r",encoding="utf") as file:
  list_str=file.readlines()
  # print(list_str)
  for el in list_str:
    if el.find("Error")!=-1:
     intError+=1  
    if el.find("Info")!=-1:
     intInfo+=1  
    print(el," ")

print(f"В файле количество лог intError = {intError} intInfo = {intInfo}")

