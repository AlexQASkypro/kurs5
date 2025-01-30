def month_to_season(month):  
    """Возвращает название сезона по номеру месяца."""  
    if month in [12, 1, 2]:  
        return "Зима"  
    elif month in [3, 4, 5]:  
        return "Весна"  
    elif month in [6, 7, 8]:  
        return "Лето"  
    elif month in [9, 10, 11]:  
        return "Осень"  
    else:  
        return "Некорректный месяц"  # Обработка некорректного значения  
  
# Запрашиваем у пользователя ввод номера месяца  
month = int(input("Введите номер месяца (1-12): "))  # Преобразуем ввод в целое число  
  
# Вызываем функцию с введённым значением месяца  
season = month_to_season(month)  
  
# Выводим результат  
print(f"Месяц {month} - это {season}.")  
