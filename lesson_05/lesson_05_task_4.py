from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Firefox
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ждем появления модального окна и кликаем на кнопку "Close"
wait = WebDriverWait(driver, 10)
close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/p")))
close_button.click()
