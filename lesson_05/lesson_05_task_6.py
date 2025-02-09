from selenium import webdriver
import time

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")
time.sleep(1)  # Пауза для визуальной проверки

# Вводим логин
username_field = driver.find_element("id", "username")
username_field.send_keys("tomsmith")
time.sleep(1)  # Пауза для визуальной проверки

# Вводим пароль
password_field = driver.find_element("id", "password")
password_field.send_keys("SuperSecretPassword!")
time.sleep(1)  # Пауза для визуальной проверки

# Нажимаем кнопку Login
login_button = driver.find_element("css selector", "button[type='submit']")
login_button.click()
time.sleep(1)  # Пауза для визуальной проверки