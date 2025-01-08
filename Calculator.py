from num_to_rus import Converter # импортирую библиотеку для перевода результата в строку

def calculator(str_main):
    # создаю словарь для последующего перевода
    dic = {'ноль': '0', 'один': '1' , 'два': '2', 'три': '3', 'четыре': '4', 'пять': '5', 'шесть': '6',
'семь': '7', 'восемь': '8', 'девять': '9', 'десять': '10', 'одиннадцать': '11',
'двенадцать': '12', 'тринадцать': '13', 'четырнадцать': '14', 'пятнадцать': '15', 'шестнадцать': '16',
'семнадцать': '17', 'восемнадцать': '18', 'девятнадцать': '19', 'двадцать': '20',
'тридцать': '30', 'сорок': '40', 'пятьдесят': '50', 'шестьдесят': '60', 'семьдесят': '70',
'восемьдесят': '80', 'девяносто': '90', 'сто': '100', 'двести': '200', 'триста': '300',
'четыреста': '400', 'пятьсот': '500', 'шестьсот': '600', 'семьсот': '700', 'восемьсот': '800',
'девятьсот': '900', 'одна тысяча': '1000', 'две тысячи': '2000', 'три тысячи': '3000',
'четыре тысячи': '4000', 'пять тысяч': '5000', 'шесть тысяч': '6000', 'семь тысяч': '7000',
'восемь тысяч': '8000', 'девять тысяч': '9000', 'минус': '-', 'плюс': '+', 'умножить': '*', 'на': '',
'открывается': '(', 'закрывается': ')', 'скобка': ''}

    # проверки
    lst_num_else = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '=', '-', '*', '/', ':', '  ']
    list_check = str_main.split()
    for el1 in list_check:
        if len(list_check) < 3 or el1 not in dic or el1 in lst_num_else:
            return 'ОШИБКА!!! Введите строку в соответствии с требованиями!'

    if str_main == '':
        return 'ОШИБКА!!! Введите строку в соответствии с требованиями!'

    if str_main == 'писят два':
        return 'ЭТО ВТОРОООООООООООООЙ'

    # пример1: девяносто девять умножить на тридцать пять
    # пример2: пять плюс семь
    # пример3: двадцать пять минус четыре
    # пример4: семь плюс тридцать два умножить на три
    # пример5: скобка открывается пять плюс три скобка закрывается умножить на два

    # на основе примеров я понимаю, как я должен построить алгоритм программы:
    # перевожу буквенную строку в числовую строку и передаю это методу eval()

    # перевожу из буквенного вида в цифровой
    str_res = ''
    for el in range(0, len(list_check)):
        # print(dic[list_check[el]])
        if list_check[el] in dic:
            if dic[list_check[el]].isnumeric():
                if dic[list_check[el-1]].isnumeric() and el > 0:
                    pass
                elif el != (len(list_check)-1):
                    if list_check[el+1] in dic:
                        if dic[list_check[el+1]].isnumeric():
                            str_res += str(int(dic[list_check[el]]) + int(dic[list_check[el+1]]))
                        else:
                            str_res += dic[list_check[el]]
                    else:
                        return 'ОШИБКА!!! Введите строку в соответствии с требованиями!'
                else:
                    str_res += dic[list_check[el]]
            else:
                str_res += dic[list_check[el]]
        else:
            return 'ОШИБКА!!! Введите строку в соответствии с требованиями!'

    res_eval_str = str(eval(str_res)) # передаю цифровую строку для вычисления результата

    # проверка скобок
    if str_res.count('(') != str_res.count(')'):
        return 'неверное количество скобок!!!'


    # функция для перевода цифрового результата в буквенный
    def number_to_text(num):
        conv = Converter()
        return conv.convert(int(num))

    # итоговый вывод из функции
    return number_to_text(res_eval_str)

str_main = input()
print(calculator(str_main))

# 1
def st_words(filename):
  """

  """
  with open(filename, 'r') as file:
    text = file.read().lower()
    for el in text:
      if el.isalpha() == False:
        text = text.replace(el, ' ')

    text = text.split()

    for el in text:
      if el.isalpha() == False:
        text.remove(el)

    dic = {key: text.count(key) for key in text}
    lst = [(val, key) for key, val in dic.items()]
    

  with open(filename + '_new', 'w') as file2:
    try:  
      while True:   
        maxx = max(lst)
        file2.write(f'Слово {maxx[1]}, кличество повторений этого слова {maxx[0]}\n')
        lst.remove(max(lst))
    except ValueError:
      print('Конец')  


print(st_words(input('Введите имя файла: ')))

# 2
import random
n = int(input('Введите размер мматрицы NxN: '))
matrix = [[random.randint(-100, 100) for _ in range(n)] for _ in range(n)]
print(matrix)

sum1, sum2 = [], []
for ind in range(n):
  if matrix[ind][ind] > 0: sum1.append(matrix[ind][ind])
  if matrix[ind][ind] < 0: sum2.append(matrix[ind][-ind-1])

if len(sum1) == 0:
  res1 = 0
else:
  res1 = sum(sum1) / len(sum1)

if len(sum2) == 0:
  res2 = 0
else:
  res2 = sum(sum2) / len(sum2)  

#среднее арифметическое / n

#3
import math

# Лямбда-функция для вычисления радиуса по площади
calculate_radius = lambda area: math.sqrt(area / math.pi)

# Лямбда-функция для вычисления длины окружности по площади
calculate_circumference = lambda area: 2 * math.pi * math.sqrt(area / math.pi)

# Примеры использования:
area = 25 # Площадь круга

radius = calculate_radius(area) # Вычисляем радиус
circumference = calculate_circumference(area) # Вычисляем длину окружности

print(f"Площадь круга: {area}")
print(f"Радиус круга: {radius:.2f}")  # Выводим радиус с 2 знаками после запятой
print(f"Длина окружности: {circumference:.2f}") # Выводим длину окружности с 2 знаками после запятой
