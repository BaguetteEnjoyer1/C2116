import random
import math

# Привітання користувача (1)
name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
print(f"Привіт {name}, тобі {age}!")

'''# Перевірка віку (2)
age = int(input("Введіть ваш вік: "))
if age >= 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

# Вгадай число (3)
number = random.randint(1, 10)
attempts = 3
for _ in range(attempts):
    guess = int(input("Вгадай число від 1 до 10: "))
    if guess > number:
        print("Менше")
    elif guess < number:
        print("Більше")
    else:
        print("Вітаю, ви вгадали!")
        break
else:
    print(f"Ви програли! Загадане число було {number}.")

# Вивід чисел у діапазоні (4)
start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))
for i in range(start, end + 1):
    print(i, end=" ")
print()

# Парні числа у зворотному порядку (5)
n = int(input("Введіть число n: "))
for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Факторіал числа (6)
n = int(input("Введіть число для обчислення факторіалу: "))
print(f"Факторіал {n} дорівнює {math.factorial(n)}")

# Оцінка студента (7)
score = int(input("Введіть кількість балів: "))
if 0 <= score <= 49:
    print("Незадовільно")
elif 50 <= score <= 69:
    print("Задовільно")
elif 70 <= score <= 89:
    print("Добре")
elif 90 <= score <= 100:
    print("Відмінно")
else:
    print("Некоректні дані")

# Калькулятор (8)
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть дію (+, -, *, /): ")
if operation == '+':
    print(f"Результат: {a + b}")
elif operation == '-':
    print(f"Результат: {a - b}")
elif operation == '*':
    print(f"Результат: {a * b}")
elif operation == '/':
    if b == 0:
        print("Ділення на нуль")
    else:
        print(f"Результат: {a / b}")
else:
    print("Некоректна операція")'''
