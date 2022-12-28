#                            ЗАДЧИ К СЕМИНАРУ 4

# ЗАДАЧА 1. Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# print("Pi =", pi)
# d = float(input("Enter the required calculation accuracy: "))
# m = 1
# newPi = 0

# while pi - newPi> d:
#     newPi = sum(1/16** x * (4 / (8 * x + 1)
#     - 2 / (8 * x + 4) 
#     - 1 / (8 * x + 5)
#     - 1 / (8 * x + 6)) for x in range(m))
#     m +=1

# print("The number of Pi with the specified accuracy =", newPi)

# ЗАДАЧА 2. Задайте натуральное число N. Напишите программу, 
#           которая составит список простых множителей числа N

# def CheckPrime(n):
#     temp = 0
#     for i in range(2, int(n**0.5)+1):
#          if (n % i == 0):
#             temp += 1
#     if temp == 0:
#         return True
#     else:
#         return False

# def Conclusion():
#     N = 5111
#     print(f"Prime factors of a number {N}:")
#     for i in range(1, N+1):
#         if N % i == 0:
#             if CheckPrime(i):
#                 print(i, end=' ')

# Conclusion()
# print()

# ЗАДЧА 3. Задайте последовательность чисел. Напишите программу, 
#          которая выведет список неповторяющихся элементов исходной последовательности

# from random import randint

# def GenlList(n):
#     genList = []
#     for i in range(n):
#         genList.append(randint(0, 10))
#     return genList

# def SetList():
#     list = GenlList(10)
#     setList = set(list)
#     print(f'The original sequence: {list}')
#     print(f'Non-repeating elements of the original sequence: {setList}')

# def OriginList():
#     originList = []
#     list = GenlList(10)
#     print(f'The original sequence: {list}')
#     for i in range(10):
#         if not(list[i] in list[i+1:] or list[i] in list[:i]):
#             originList.append(list[i])
#     print(f'list of non-repeating elements of the original sequence: {originList}') 

# SetList()
# OriginList()

# ЗАДАЧА 4. Задана натуральная степень k. 
#           Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
#           многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# k = 3
# def GenPolyString(n):
#     poly = ""
#     for i in range(n, -1, -1):
#         rnd = randint(0,100)
#         if rnd != 0:
#             if len(poly) > 1:
#                poly += " + "
#             if i == 0:
#               poly += str(rnd)
#             else:
#                 poly += str(rnd) + "*x**" + str(i)
#     poly += " = 0"
#     return poly

# def String():
#     polynom = GenPolyString(k)
#     print("Random polynomial:", polynom)
#     with open("polynom.txt", "w") as file:
#         file.write(polynom)

# String()

# ЗАДАЧА 5. Даны два файла, в каждом из которых находится запись многочлена. 
#           Задача - сформировать файл, содержащий сумму многочленов

# def ParsePoly(string):
#     my_list = list(string.split())
#     for i in my_list:
#         if "+" in my_list:
#             my_list.remove("+")
#         if "=" in my_list:
#             my_list.remove("=")
#     my_list.pop()
#     return my_list

# def readFromFile(file):
#     data = ""
#     with open(file) as rfile:
#         data = rfile.read()
#     return data

# def dictToFile(mydict, file3):
#     new_poly = ""
#     for i in reversed(mydict.items()):
#         if i[0] == 0:
#             new_poly += str(i[1]) + " + "
#         else:
#             new_poly += str(i[1]) + "*x**" + str(i[0]) + " + "

#     new_poly = new_poly[:-3]

#     with open(file3, "w") as newfile:
#         print(f"Записываем в файл {file3} новый полином: {new_poly}")
#         newfile.write(new_poly)
#     return

# def makeDict(poly_list):
#     poly_dict = {}
#     poly_list.reverse()
#     for item in poly_list:
#         if item.isdigit():
#             poly_dict[0] = int(item)
#         else:
#             poly_dict[int(item.split("**")[-1])] = int(item[0:item.find("*")])
#     return poly_dict

# def sum_dict(dict1, dict2):
#     for key, value in dict1.items():
#         dict1[key] = value + dict2.get(key, 0)
#     return dict1

# def main():
#     poly1 = readFromFile("polynom.txt")
#     print("Полином 1:", poly1)
#     poly2 = readFromFile("polynom2.txt")
#     print("Полином 2:", poly2)

#     print("Полином 1, преобразованный в список:", ParsePoly(poly1))
#     print("Полином 2, преобразованный в список:", ParsePoly(poly2))

#     poly_dict1 = makeDict(ParsePoly(poly1))
#     poly_dict2 = makeDict(ParsePoly(poly2))

#     print("Парсим сумму полиномов в словарь:", sum_dict(poly_dict1, poly_dict2))
    
#     dictToFile(poly_dict1, "polynom3.txt")

# if __name__ == "__main__":
#     main()