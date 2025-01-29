def is_year_leap(year):  
    """  
    Проверяет, является ли год високосным.  
      
    :param year: Год (число)  
    :return: True, если год високосный, иначе False  
    """  
    return year % 4 == 0  
  
# Выбор года для проверки  
year_to_check = 2022  # Вы можете изменить этот год на любой другой  
  
# Вызов функции и сохранение результата в переменной  
is_leap = is_year_leap(year_to_check)  
  
# Вывод результата в консоль  
print(f'Год {year_to_check}: {is_leap}')  