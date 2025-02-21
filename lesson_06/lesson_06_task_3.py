from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # 1. Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # 2. Ожидание завершения загрузки
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
    )
    
    # 3. Получение 3-й картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    third_image_src = images[2].get_attribute("src")
    
    # 4. Вывод результата
    print("SRC третьей картинки:", third_image_src)

finally:
    # Закрытие браузера
    driver.quit()
    