#Coupling is basically a thing , in which we are telling our classes to have 
#loosely coupled logic , this will help us in future when even if we have to 
# add some new implementation to doing our current thing , without having to change
# in main code , so this things can be handled in backend using interface 

# sadly , In python we don't have interface but we do have the abstract classes 
# so we can use abstract class as interface in reference and achieve the same behaviour

#Below is one example of same where i am sending notification when the order is placed 
# without tightly coupling the logic about how and which way i will send like Email,SMS,Slack etc.
# According to your needs add the implementations which will implement main NotificationService
# without changing the main code in the order class 

from abc import ABC,abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass
    
class EmailSender(NotificationService):
    def __init__(self):
        print("Email sender initialized")
    def send_notification(self, message):
        print("Email sent successfully :"+ message)


class Order:
    def __init__(self):
        print("Order initiated successfully")
    def place_order(self,notification_type,message):
        notification_type.send_notification(message)    

order=Order()
order.place_order(EmailSender() ,"this is sample message")
