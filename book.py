import pandas as pd

class Book:
    def __init__(self,name):
        self.name=name
        self.idOrder=1
        self.listOfOrders=[[],[]]

    def insert_buy(self,number,price):
        print("--- Insert BUY "+ str(number)+"@"+str(price)+" id="+str(self.idOrder)+" on "+str(self.name))
        newOrder=Order(self.idOrder,"BUY",number,price)
        self.idOrder+=1
        newOrder=self.tryExecute(newOrder,self.listOfOrders[1])
        if(newOrder!=None):
            if(len(self.listOfOrders[0])!=0):
                indexList=[self.listOfOrders[0].index(x) if x.price>=newOrder.price else -1 for x in self.listOfOrders[0]]
                self.listOfOrders[0].insert((max(indexList)+1),newOrder)
            else:
                self.listOfOrders[0].append(newOrder)
        
        self.displayBook()

    def insert_sell(self,number,price):
        print("--- Insert SELL "+ str(number)+"@"+str(price)+" id="+str(self.idOrder)+" on "+str(self.name))
        newOrder=Order(self.idOrder,"SELL",number,price)
        self.idOrder+=1
        newOrder=self.tryExecute(newOrder,self.listOfOrders[0])
        if(newOrder!=None):
            if(len(self.listOfOrders[1])!=0):
                indexList=[self.listOfOrders[1].index(x) if x.price<=newOrder.price else -1 for x in self.listOfOrders[0]]
                self.listOfOrders[1].insert((max(indexList)+1),newOrder)
            else:
                self.listOfOrders[1].append(newOrder)
    
        self.displayBook()

    def displayBook(self):
        if(len(self.listOfOrders[1]) !=0):
            dfSell=pd.DataFrame.from_records([x.to_dict() for x in self.listOfOrders[1]],index=[i.id for i in self.listOfOrders[1]])
            print(dfSell)
            print()
        if(len(self.listOfOrders[0]) !=0): 
            dfBuy=pd.DataFrame.from_records([x.to_dict() for x in self.listOfOrders[0]],index=[i.id for i in self.listOfOrders[0]])
            print(dfBuy)
            print()
        '''
        print("Book on " +str(self.name))
        for i in range(len(self.listOfOrders[1])-1,-1,-1):
            print("\t"+str(self.listOfOrders[1][i].type)+" "+str(self.listOfOrders[1][i].number)+"@"+str(self.listOfOrders[1][i].price)+" id="+str(self.listOfOrders[1][i].id))
        for i in range(len(self.listOfOrders[0])):
            print("\t"+str(self.listOfOrders[0][i].type)+" "+str(self.listOfOrders[0][i].number)+"@"+str(self.listOfOrders[0][i].price)+" id="+str(self.listOfOrders[0][i].id)) 
        print("------------------------------")
        '''

        
    def tryExecute(self,order,listOfOrders):
        if(len(listOfOrders)!=0):
            if(order.type=="BUY"):
                if (order.price >= listOfOrders[0].price):
                    while(order.price>= listOfOrders[0].price):
                        if(order.number< listOfOrders[0].number):
                            listOfOrders[0].number-=order.number
                            print("Execute "+str(order.number) + " at "+str(listOfOrders[0].price)+" on " +str(self.name))
                            order.number=0
                            break
                        elif(order.number >= listOfOrders[0].number):
                            print("Execute "+str(listOfOrders[0].number) + " at "+str(listOfOrders[0].price)+" on " +str(self.name))
                            order.number-=listOfOrders[0].number
                            listOfOrders.pop(0)
                    if(order.number==0):
                        toReturn=None
                    elif(order.number>0):
                        toReturn=order
                    else:
                        print("Erreur")
                else:
                    toReturn=order
            elif(order.type=="SELL"):
                if (order.price <= listOfOrders[0].price):
                    while(order.price<= listOfOrders[0].price):
                        if(order.number< listOfOrders[0].number):
                            listOfOrders[0].number-=order.number
                            print("Execute "+str(order.number) + " at "+str(listOfOrders[0].price)+" on " +str(self.name))
                            order.number=0
                            break
                        elif(order.number >= listOfOrders[0].number):
                            print("Execute "+str(listOfOrders[0].number) + " at "+str(listOfOrders[0].price)+" on " +str(self.name))
                            order.number-=listOfOrders[0].number
                            listOfOrders.pop(0)
                    if(order.number==0):
                        toReturn=None
                    elif(order.number>0):
                        toReturn=order
                    else:
                        print("Erreur SELL")
                else:
                    toReturn=order
        else:
            toReturn=order

        return toReturn

                        
class Order:
    def __init__(self,idOrder,typeOrder,number,price):
        self.id=idOrder
        self.type=typeOrder
        self.number=number
        self.price=price
    def to_dict(self):
        return {
                'Type': self.type,
                'Number':self.number,
                'Price': self.price,
                 }
