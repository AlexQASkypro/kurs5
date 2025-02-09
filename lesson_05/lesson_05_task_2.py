from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

# Инициализация драйвера
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Находим синюю кнопку по классу и кликаем на неё
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

sleep(10)