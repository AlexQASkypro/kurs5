from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликнуть на кнопку "Add Element"
for _ in range(5):
    driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()

# Собрать список кнопок "Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

# Вывести размер списка кнопок "Delete"
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

sleep(10)