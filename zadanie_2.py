def read_numbers(count):
    numbers_set = set()
    for _ in range(count):
        number = int(input("Введите число: "))
        numbers_set.add(number)
    return numbers_set

# Считываем количество чисел в первом списке
n1 = int(input("Введите количество чисел в первом списке: "))
print("Ввод чисел первого списка:")
list1 = read_numbers(n1)

# Считываем количество чисел во втором списке
n2 = int(input("Введите количество чисел во втором списке: "))
print("Ввод чисел второго списка:")
list2 = read_numbers(n2)

# Находим пересечение множеств
common_elements = list1.intersection(list2)

# Выводим количество общих элементов
print("Количество общих чисел:", len(common_elements))
