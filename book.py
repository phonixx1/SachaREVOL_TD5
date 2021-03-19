import pandas as pd

class Book:
    def __init__(self,name):  # initialisation of book class
        self.name=name        # name of book
        self.idOrder=1        # id index init
        self.listOfOrders=[[],[]]  # body of book

    def insert_buy(self,number,price):
        print("--- Insert BUY "+ str(number)+"@"+str(price)+" id="+str(self.idOrder)+" on "+str(self.name))
        newOrder=Order(self.idOrder,"BUY",number,price)
        self.idOrder+=1
        newOrder=self.tryExecute(newOrder,self.listOfOrders[1])   #try to execute the new order : will try to execute  with the order which alredy exist on the book ( if some order match)
        if(newOrder!=None):                                       # here we tchek if newOrder is diff to None because last function return NONE if the new order is totaly executed with order of the book
            if(len(self.listOfOrders[0])!=0):                   # so we add a part of the new order to the book
                indexList=[self.listOfOrders[0].index(x) if x.price>=newOrder.price else -1 for x in self.listOfOrders[0]] # we search the position of the new order on the book
                self.listOfOrders[0].insert((max(indexList)+1),newOrder)
            else:
                self.listOfOrders[0].append(newOrder)  # just the case of empty book
        
        self.displayBook()

    def insert_sell(self,number,price): # same logic but for selling
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

    def displayBook(self):  # display of the book with pandas data frame. We put in comment our old display ask in Ex3
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
        if(len(listOfOrders)!=0):               # list empty ?
            if(order.type=="BUY"):              # if not what type of order
                if (order.price >= listOfOrders[0].price):      #the main condition : if out buying price is higher of the lower selling price we will execute
                    while(order.price>= listOfOrders[0].price):     # here we will try to execute as much as possible our new order......
                        if(order.number< listOfOrders[0].number):   # .... depending of the available quantity
                            listOfOrders[0].number-=order.number
                            print("Execute "+str(order.number) + " at "+str(listOfOrders[0].price)+" on " +str(self.name))
                            order.number=0
                            break
                        elif(order.number >= listOfOrders[0].number):
                            print("Execute "+str(listOfOrders[0].number) + " at "+str(listOfOrders[0].price)+" on " +str(self.name))
                            order.number-=listOfOrders[0].number
                            listOfOrders.pop(0)
                    if(order.number==0):              # if all the new order is execute
                        toReturn=None
                    elif(order.number>0):               # if we execute nothing or just a part of the new order
                        toReturn=order
                    else:
                        print("Erreur")
                else:
                    toReturn=order
            elif(order.type=="SELL"):                               # same logic for selling
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
    def to_dict(self):     # we create this function to implement easely the pandas df
        return {
                'Type': self.type,
                'Number':self.number,
                'Price': self.price,
                 }
