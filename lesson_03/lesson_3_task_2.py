from smartphone import Smartphone  
  
# Создаем переменную catalog и наполняем ее экземплярами класса Smartphone  
catalog = [  
    Smartphone("Apple", "iPhone 14", "+79001234567"),  
    Smartphone("Samsung", "Galaxy S21", "+79002345678"),  
    Smartphone("Xiaomi", "Redmi Note 10", "+79003456789"),  
    Smartphone("Huawei", "P40 Pro", "+79004567890"),  
    Smartphone("Google", "Pixel 6", "+79005678901")  
]  
  
# Печатаем весь каталог в нужном формате  
for smartphone in catalog:  
    print(smartphone)  