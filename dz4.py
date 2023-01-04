#Вычислить число c заданной точностью d. 
 #	Пример:
 #	при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10).
 	 
#from math import pi
#d = int(input("Введите число для заданной точности числа Пи:\n"))
#print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#def number_(n: int):
 #   i = 2
  #  while n % i != 0 or i == n - 1:
   #     i += 1
    #if i == n:
     #   return n

#def fill_my_list(n: int) -> list:
#    my_list = [1]
 #   for i in range(2, n+1):
  #      if n % i == 0:
   #         if number_(i) != None:
    #            my_list.append(number_(i))
     #       else:
      #          continue
    #return my_list

# n = int(input('Введите натуральное число N: '))
# my_list = fill_my_list(n)
# print(my_list)


#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# my_list = list(map(int, input("Введите числа через пробел:\n").split()))
# new_list = []
# [new_list.append(i) for i in my_list if i not in new_list]
 	
# print(f"Список из неповторяющихся элементов: {new_list}")

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


# from random import randint
# print('Введите натуральную степень k:')
# k = int(input())
 
# def write_file(st):
#     with open('file44.txt', 'w') as data:
#         data.write(st)
 
# def create_list(k):
#     list = []
#     for i in range(k + 1):
#         list.append(randint(0, 101))    
#     return list
    
# def create_str(sp):
#     list = sp[::-1]
#     wr = ''
#     if len(list) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(list)):
#             if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
#                 wr += f'{list[i]}x^{len(list) - i - 1}'
#                 if list [i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 2 and list[i] != 0:
#                 wr += f'{list[i]}x'
#                 if list[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 1 and list[i] != 0:
#                 wr += f'{list[i]} = 0'
#             elif i == len(list) - 1 and list[i] == 0:
#                 wr += ' = 0'
#     return wr
 
#koef = create_list(k)
#write_file(create_str(koef))

#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# with open('myfile_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('myfile_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('myfile_1.txt','r') as file:
#     my_1 = file.readline()
#     list_of_my_1 = my_1.split()


# with open('myfile_2.txt','r') as file:
#     my_2 = file.readline()
#     list_of_my_2 = my_2.split()

# print(f'{list_of_my_1} + {list_of_my_2}')
# sum = list_of_my_1 + list_of_my_2

# with open('sum_file.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_my_1} + {list_of_my_2}')