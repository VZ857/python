
# Удаление абв
# str = 'Привет абв мир ,я любабвлю питонабв'
# print ("Исходная строка: " + str) 
# res_str = str.replace('абв', '') 
# print("Строка после удаления всех символов абв: " + res_str) 

# Удаление через for
# str = 'Привет абв мир ,я любабвлю питонабв'
# print(f"Исходный текст: {str}")
# find_txt = "абв"
# lst = [i for i in str.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')


# Удаление с помощью filter

str = 'Привет абв мир ,я любабвлю питонабв'
def delet(str):
    str = list(filter(lambda i: 'абв' not in i, str.split()))
    return " ".join(str)

str = delet(str)

print(str)