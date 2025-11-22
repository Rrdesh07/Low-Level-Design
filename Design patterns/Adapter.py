#Adapter pattern

#when to use ?
#--> We can use this when we have two classes which are different but we have to 
# --> itegrate them to work our business logic ,since they are different we can't 
# --> directly use them , so we have to create adapater class in between them.

#why to use ?
# --> To workout the difference between two classes without changing their code 
# --> Instead of this we write our own adapter class and help these two classes to 
# --> interact with each other easily.


class BankService:
    def make_payment(self,amount):
        print(f"Processing payment of {amount} using bank service")
        
class PaymentService:
    def pay(self,amount):
        pass 

class BankServiceAdapter(PaymentService):
    def __init__(self,BankService):
        self.BankService=BankService
        
    def pay(self,amount):
        self.BankService.make_payment(amount)

def process_payment(payment_service,amount):
    payment_service.pay(amount)


bank_service_adapter=BankServiceAdapter(BankService())
process_payment(bank_service_adapter,100)    
