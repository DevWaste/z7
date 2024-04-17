# Ввод данных
numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

# Отслеживание уже встреченных чисел
seen = set()
for number in numbers:
    if number in seen:
        print(f"{number} YES")  # Число уже встречалось
    else:
        print(f"{number} NO")  # Число встречается впервые
        seen.add(number)