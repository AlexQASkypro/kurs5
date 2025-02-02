from address import Address  
  
class Mailing:  
    def __init__(self, to_address, from_address, cost, track):  
        self.to_address = to_address  # Тип данных Address  
        self.from_address = from_address  # Тип данных Address  
        self.cost = cost  # Число  
        self.track = track  # Строка  
  
    def __str__(self):  
        return (      
            f"Отправление {self.track} из {self.from_address} в {self.to_address}. "  
            f"Стоимость {self.cost} рублей."  
        )  