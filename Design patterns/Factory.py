# Factory Pattern 

# when to use ?
# --> when you have to create similar objects with normal difference 
# --> Instead of tight coupling by creating direct objects in main function code 
# --> use factory to save you in that case 

# why to use ?
#--> To basically provide runtime flexibility to change the creational object 
#--> loosely couple our code and increase the flexibility 

from abc import ABC,abstractmethod

class pizza(ABC):
    
    @abstractmethod
    def prepare (self):
        pass
        
class CheesePizza(pizza):
    def prepare(self):
        print("Cheese pizza is prepared")

class PepperoniPizza(pizza):
    def prepare(self):
        print("Pepperoni Pizza is prepared")
        
class VeggiePizza(pizza):
    def prepare(self):
        print("Veggie Pizza is prepared")
        

class PizzaFactory:
    @staticmethod
    def create_order(pizzaType):
        if pizzaType == "cheese":
            return CheesePizza()
        elif pizzaType == "pepperoni":
            return PepperoniPizza()
        elif pizzaType == "veggie":
            return VeggiePizza()
        else: 
            raise ValueError(f" Unkown Pizza type :{pizzaType}") 
        
            
def main():
    try:
        user_input="cheese"
        pizza=PizzaFactory.create_order(user_input)
        pizza.prepare()
    except Exception as e:
        print(e)

main()