#Зайти на labirint.ru
#найти книги по слову python
# собрать все карточки товаров
# вывести в консоль информацию: название + автор + цена


from time import sleep
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

driver = webdriver.Chrome()
# зайти на сайт лабиринт
driver.get("https://labirint.ru")

# найти все книги по слову python
search_locator = '#search-field'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python", Keys.RETURN) 

#собрать все карточки локаторов
driver.find_elements(By.CSS_SELECTOR, "div.product-card")
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

# вывести в консоль инфо: название + автор + цена
# for book in books:
# 	title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
# 	price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
# 	author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
	

# print(author + "\t" + title + "\t" + price)

for book in books:
    try:
        # Название книги
        title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text.strip()
        
        # Автор книги
        author_element = book.find_elements(By.CSS_SELECTOR, "div.product-card__author")
        author = author_element[0].text.strip() if author_element else "Автор не указан"
        
        # Цена книги
        price_element = book.find_elements(By.CSS_SELECTOR, "div.product-card__price-current")
        price = price_element[0].text.strip() if price_element else "Цена не указана"
        
        # Вывод информации
        print(f"Название: {title}")
        print(f"Автор: {author}")
        print(f"Цена: {price}")
        print("-" * 40)
    except Exception as e:
        print(f"Ошибка при парсинге книги: {e}")

sleep(5)