

    # Напишите программу, которая найдёт произведение пар чисел списка. 
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# МАР
def pro(lst):
    n = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    lst = [lst[i]*lst[len(lst)-i-1] for i in range(n)]
    print(lst)

        
lst = list(map(int, input("Введите числа через запятую: ").split(',')))
pro(lst)

