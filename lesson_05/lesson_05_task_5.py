from selenium import webdriver
import time

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода и вводим текст 1000
input_field = driver.find_element("tag name", "input")
input_field.send_keys("1000")

# Пауза 2 секунды (для визуальной проверки)
time.sleep(2)

# Очищаем поле
input_field.clear()

# Пауза 2 секунды (для визуальной проверки)
time.sleep(2)

# Вводим текст 999
input_field.send_keys("999")

# Пауза 2 секунды (для визуальной проверки)
time.sleep(2)