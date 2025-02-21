from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера с использованием Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Закрыты все скобки

try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ожидание загрузки всех картинок
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "image-container"))
    )
    
    # Получение всех изображений
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    
    # Проверка, что изображений достаточно
    if len(images) >= 3:
        third_image = images[2]  # Индексация начинается с 0
        print(third_image.get_attribute("src"))
    else:
        print("Третье изображение не найдено.")
    
finally:
    # Закрытие браузера
    driver.quit()
    