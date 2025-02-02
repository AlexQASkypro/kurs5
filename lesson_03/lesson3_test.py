from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()


card = Card("4353 1234 5678 9012", "11/28", "Alex A")
alex.addCard(card)
card.pay(1000)
