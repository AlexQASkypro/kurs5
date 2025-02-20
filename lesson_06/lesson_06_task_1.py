from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера с использованием Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")
    
    # Нажатие на синюю кнопку
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    
    # Ожидание появления зеленой плашки и получение текста
    green_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    print(green_label.text)
    
finally:
    # Закрытие браузера
    driver.quit()