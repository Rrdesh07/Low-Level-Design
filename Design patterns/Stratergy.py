#Stratergy pattern 

#when to use ?
# --> when you have lot of stratergies and you want to choose which algo or stratergy
# --> dynamically without modifying the main client code.

# why to use ?
# --> It provides scalable , flexible way to add new startergies to the existing ones
# --> without even changing the previous code , which follows Open-Close principle.

from abc import ABC,abstractmethod

class PaymentStratergy(ABC):
    @staticmethod
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentStratergy):
    def __init__(self):
        print("Usign Credit Card Payment stratergy")
        
    def pay(self,amount):
        print(f"Managing payment of {amount} with Credit Card")
        

class PayPalPayment(PaymentStratergy):
    def __init__(self):
        print(" Using Paypal payment stratergy")
        
    def pay(self,amount):
        print(f"Managing payment of {amount} using paypal")
        
class CryptoPayment(PaymentStratergy):
    def __init__(self):
        print(" Using Crypto payment stratergy ")
        
    def pay(self,amount):
        print(f"Managing payment of {amount} using Crypto Currency")
        
class PaymentProcessor:
    def __init__(self,PaymentStratergy):
        print("Initializing the payment processor")
        self.PaymentStratergy=PaymentStratergy
    
    def set_stratergy(self,PaymentStratergy):
        self.PaymentStratergy=PaymentStratergy
        
    def process_payment(self,amount):
        self.PaymentStratergy.pay(amount)
        

def main ():
    payment_processor = PaymentProcessor(CreditCardPayment())
    payment_processor.process_payment(100)
    
    payment_processor.set_stratergy(PayPalPayment())
    payment_processor.process_payment(50)
    
    payment_processor.set_stratergy(CryptoPayment())
    payment_processor.process_payment(500)
    
    
main()