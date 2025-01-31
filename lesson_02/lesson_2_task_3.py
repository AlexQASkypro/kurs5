import math  
  
def square(side):  
    """Вычисляет площадь квадрата."""  
    area = side * side  
    return math.ceil(area)  
  
# Запрашиваем у пользователя ввод стороны квадрата  
side_input = float(input("Введите длину стороны квадрата: "))  
  
# Вызываем функцию и сохраняем результат в переменной  
area_result = square(side_input)  
  
# Выводим результат  
print(f"Площадь квадрата со стороной {side_input}: {area_result}")  
