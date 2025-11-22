#Observer pattern 

#when to use?
#--> Observer pattern is used where you have pub -sub model
#--> when there is one publisher who publishes the data 
#--> now subscribers needs to updated to the latest published data 
#--> sort of similar to how kafka , rabbitmq generally works in real life 

# where we can use ?
#--> stock update , youtube subscribe model

# why to use ?
#--> simplifies the process of updating the observers with latest published data 
#--> loose coupling code 


from abc import ABC,abstractmethod

class Stock:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.observers=[]
    
    def add_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self)
            
    def set_price(self,price):
        self.price=price
        self.notify_observer()
        
class Observer(ABC):
    @abstractmethod
    def update(self,stock):
        pass

class Dashboard(Observer):
    def update(self,stock):
        print(f"Dashboard updated: {stock.name} price is updated to {stock.price}")
         
class EmailAlert(Observer):
    def update(self,stock):
        print(f"Email sent: {stock.name} price is updated to {stock.price}")
        
class SMSAlert(Observer):
    def update(self,stock):
        print(f"SMS sent : {stock.name} price is updated to {stock.price}")


apple_stock=Stock("Apple",200)
jio_stock=Stock("Jio",2)

dashboard=Dashboard()
email=EmailAlert()
sms=SMSAlert()

apple_stock.add_observer(dashboard)
jio_stock.add_observer(email)
apple_stock.add_observer(sms)

apple_stock.set_price(300)
jio_stock.set_price(-5)
