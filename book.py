

class Book:
    def __init__(name):
        self.name=name
        self.idOrder=1
        self.listOfOrders=[]

    def insert_buy(number,price):
        listOfOrders.append(Order(self.idOrder,"BUY",number,price))
        self.Order+=1

    def insert_sell(number,price):
        listOfOrders.append(Order(self.idOrder,"SELL",number,price))
        self.Order+=1

    def displayBook():
        return 0

    
class Order:
    def __init__(id,type,number,price):
        self.id=id
        self.number=number
        self.price=price

