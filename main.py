# Создать программу в которой пользователь вводит 2 числа и ему возвращается результат деления этих чисел, после вопрос хочет ли он повторить.
# При выполнении программы записывать ее выполнение в лог файл. Если не было исключений записать лог с типом Info с сообщением вводимых чисел и результата.
# Если возникло исключение - с типом Error и сообщением какое исключение было вызвано.
# Когда пользователь на вопрос хочет ли он повторить ответит "нет" прочитать файл логов и вывести на экран кол-во с типом Info и кол-во с типом Error
import datetime
print("Hello word")
print("Данная программа производить деление одного деления на другое и выводить значение в лог файл")
# with open("lesson.log", mode="a", encoding="utf") as file:
try:
 a=int(input("Введите первое число= "))  
except ValueError:
 print(f'Error при вводе первого числа вы ввели не число {datetime.datetime.now()}')
 exit();
try:
 b=int(input("Введите второе число= "))  
except ValueError:
 print(f'Error при вводе второго числа вы ввели не число {datetime.datetime.now()}')
 exit
finally:
 pass   

try:
 c=a/b
except ZeroDivisionError:
 print(f'Error при вводе второго числа вы ввели не число {datetime.datetime.now()}')   
 exit
print(f"Результат деления {a}/{b}={c} {datetime.datetime.now()}")

         

#  file.write(f"Error {ValueError.__str__} ")   
# ... except Exception:
# ...     print('Это что ещё такое?')

#  try:
  
#  except:
# except ZeroDivisionError:
#   print(f"Вы ввели не число")     
#  finally:
#   print(f"Вы ввели число={a}")   
