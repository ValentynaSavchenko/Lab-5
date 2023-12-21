"""
Задача №2

В олімпіаді з інформатики брало участь кілька осіб. Визначте кількість
школярів, які стали переможцями в кожному класі. Переможцями
оголошуються всі, хто набрав найбільшу кількість балів по даному класу.
Гарантується, що в кожному класі був хоча б один учасник.
Запишіть у файл три числа в одному рядку через пропуск: кількість переможців
олімпіади з 9 класу, з 10 класу, з 11 класу.

Вхідні дані:

Файл input.txt з вмістом
Albert Einstein 9 90
Niels Bohr 9 93
Ernest Rutherford 10 91
Lev Landau 11 92
Enrico Fermi 9 93
Ivan Puluj 10 91

Вихідні дані:

Файл output.txt з вмістом
2 2 1

Автор: Савченко Валентина 31І
"""
with open('input.txt', 'r') as f:
    lines = f.readlines()
win9 = 0
win10 = 0
win11 = 0
max_9 = 0
max_10 = 0
max_11 = 0

for el in lines:
    student = el.split()
    student[2] = int(student[2])
    student[3] = int(student[3])
    
    if student[2] == 9:
        if student[3] > max_9:
            max_9 = student[3]
            win9 = 1
        elif student[3] == max_9:
            win9 += 1
            
    if student[2] == 10:
        if student[3] > max_10:
            max_10 = student[3]
            win10 = 1
        elif student[3] == max_10:
            win10 += 1
            
    if student[2] == 11:
        if student[3] > max_11:
            max_11 = student[3]
            win11 = 1
        elif student[3] == max_11:
            win11 += 1
            
with open('output.txt', 'w') as f:
    f.write(f"{win9} {win10} {win11}")
                
            
