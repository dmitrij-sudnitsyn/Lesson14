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
while s=='y':
 while True:   
  try:
   a=int(input("Введите первое число= "))  
   break
  except ValueError:
   print(f'Error при вводе первого числа вы ввели не число {datetime.datetime.now()}')
   file.writelines(f'Error при вводе первого числа вы ввели не число {datetime.datetime.now()}')
 while True:   
  try:
   b=int(input("Введите второе число= "))  
   break
  except ValueError:
   print(f'Error при вводе второго числа вы ввели не число {datetime.datetime.now()}')
   file.writelines(f'Error при вводе второго числа вы ввели не число {datetime.datetime.now()}')

 
 try:
  c=a/b
  print(f"Результат деления {a}/{b}={c} {datetime.datetime.now()}")
  file.writelines(f"info Результат деления {a} / {b} = {c} {datetime.datetime.now()}")
 except ZeroDivisionError:
  print(f'Error деление  на 0 {a}/{b} не допустимо {datetime.datetime.now()}')   
  file.writelines(f'Error деление  на 0 {a} / {b} не допустимо {datetime.datetime.now()}')

 print("Продолжим деление?")
 print("Введите Да или Y если хотите повторить")
 print("Введите Нет или n если хотите закончить")
 i=input("Продолжить? ")
 if i=="нет" or i=="n":
  s='n'  

         

#  file.write(f"Error {ValueError.__str__} ")   
# ... except Exception:
# ...     print('Это что ещё такое?')

#  try:
  
#  except:
# except ZeroDivisionError:
#   print(f"Вы ввели не число")     
#  finally:
#   print(f"Вы ввели число={a}")   
