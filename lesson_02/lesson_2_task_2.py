def is_year_leap(year):  
    """Проверяет, является ли год високосным."""  
    return year % 4 == 0  
  
# Запрашиваем у пользователя ввод года  
year_input = int(input("Введите год: "))  
  
# Вызываем функцию и сохраняем результат в переменной  
is_leap = is_year_leap(year_input)  
  
# Выводим результат  
print(f"Год {year_input}: {is_leap}")  