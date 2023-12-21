"""
Задача №1

Напишіть функцію для обчислення факторіала заданого числа.

Вхідні дані:
5
Вихідні дані:
120

Автор: Савченко Валентина 31І
"""
def factorial(num):
    if num < 0:
        raise ValueError        
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

while True:
    try:
        num = int(input("Введіть число для обчислення його факторіалу: "))
        print(factorial(num))
        break
    except ValueError:
        print("Факторіал визначено лише для додатних цілих чисел")
