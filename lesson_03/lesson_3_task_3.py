from address import Address  
from mailing import Mailing  
  
# Создаем адреса для отправления  
to_address = Address("101000", "Москва", "Тверская", "10", "5")  
from_address = Address("125009", "Москва", "Никольская", "7", "2")  
  
# Создаем экземпляр класса Mailing  
mailing = Mailing(to_address, from_address, 250.0, "TRK123456789")  
  
# Печатаем информацию об отправлении  
print(mailing)  