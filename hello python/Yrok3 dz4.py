#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.



# n = int(input('ВВедите десятичное число: ')) 
# if n > 0 :
#     n = bin(n)
#     print(n)
# else :
#     print('ошибка')

n=int(input())
while n > 0 :
    last= n % 2
    print(last)
    n=n//2


