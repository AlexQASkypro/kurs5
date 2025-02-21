from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация драйвера с использованием Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")
    
    # Ввод текста в поле ввода
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")
    
    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    
    # Получение текста кнопки и вывод в консоль
    print(blue_button.text)
    
finally:
    # Закрытие браузера
    driver.quit()
    