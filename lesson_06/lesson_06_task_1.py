from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH

try:
    # Переход на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Нажатие на синюю кнопку
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()

    # Ожидание появления текста в зеленой плашке
    green_banner = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content > p.bg-success"))
    )
    
    # Получение текста из зеленой плашки
    banner_text = green_banner.text
    print(banner_text)  # Вывод текста в консоль

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие драйвера
    driver.quit()