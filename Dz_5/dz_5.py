#Напишите программу, удаляющую из текста все слова, содержащие "абв".
# my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
# new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
# print(new_str)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


# from random import randint


# def input_kol(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, вы ввели некорректное количество: "))
#     return x


# def my_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))


# flag = randint(0, 2)  #  очередность ходов
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_kol(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         my_print(player1, k, counter1, value)
#     else:
#         k = input_kol(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         my_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

#Создайте программу для игры в ""Крестики-нолики"".

#maps = [1,2,3,4,5,6,7,8,9]
 

# victories = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 

# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 

# game_over = False
# player1 = True
 
# while game_over == False:
 
#     
#     print_maps()
 
#   
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
 
#     step_maps(step,symbol) 
#     win = get_result() 
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
 
      
# print_maps()
# print("Победил", win)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('my_file.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('my_file.txt', 'r') as data:
    string = data.readline()

with open('my_file_1.txt', 'w') as data:
   data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('my_file_1.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('my_file_1.txt', 'r') as file:
    decoded_string = file.read()

with open('my_file_1.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)


print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))



