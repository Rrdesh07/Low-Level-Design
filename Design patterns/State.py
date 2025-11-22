# State pattern

# when to use ?
# --> when you have multiple states and on this state type you have to do 
# --> some actions , in that scenario you can use state pattern which 
# --> helps you to manage the states very easily and efficiently.


# why to use ?
# --> we should use the state to make our state management functionality 
#-> make more scalable , less error prone , easy to understand , flexible 
#--> enough to add new state functionalites without changing the previous ones.

from abc import ABC,abstractmethod

class VendingMachine:
    def __init__(self):
        self.count=5
        self.ideal_state=IdealState()
        self.has_money_state=HasMoneyState()
        self.out_of_stock_state=OutOfStockState()
        self.state=self.ideal_state
        
    def handle(self,action):
        self.state.handle(self,action)
        
class State(ABC):
    @abstractmethod
    def handle(self,action):
        pass 
    
    
class IdealState(State):
    def handle(self,machine:VendingMachine,action):
        if action == "insert_coin":
            machine.state=machine.has_money_state
            print("Coin inserted. You can select a snack")
        else :
            print("Please insert a coin ,first")

class HasMoneyState(State):
    def handle(self,machine:VendingMachine,action):
        if machine.count>0 and action == "Select_Snack":
            machine.count-=1
            machine.state=machine.out_of_stock_state
            print("Dispensing your snack, Thank you !!")
        elif machine.count ==0:
            print("Sorry, Machine is out of stock!!")
        else:
            print("Please select the snack")
            
class OutOfStockState(State):
    def handle (self,machine,action):
        print("Sorry, Machine is out of stock!!")
        

def main():
    machine=VendingMachine()
    machine.handle("insert_coin")
    machine.handle("Select_Snack")
    
main()