from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://ya.ru")

driver.get("https://vk.com")

# Будем ходить туда-обратно 10 секунд потом заснем на 15 сек
# for x in range (1, 10):
#     driver.back()
#     driver.forward()

driver.set_window_size(640, 480)
sleep(15)