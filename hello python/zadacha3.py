# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

print ("Введите координату: ")
k = int(input())
if k < 1 or n > 4:
     print('Please, repeat the input')
elif k == 1:
     print('x > 0 and y > 0')
elif k == 2:
     print('x < 0 and y > 0')
elif k == 3:
     print('x < 0 and y < 0')
elif k == 4:
     print('x > 0 and y < 0')