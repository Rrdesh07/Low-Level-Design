#Singleton pattern 
# see basically for controling flights you will need only 
# one control tower right so it's correct to tell class to return 
# instance only once , Instead of creating multiples


class ControlTower:
    _instance=None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
            print("Intializing Control Tower!!")
        return cls._instance
    
    def manage_flight(self, flight):
        print(f" Managing flight :{flight}")
        
tower1=ControlTower()
tower2=ControlTower()

tower1.manage_flight("hello")
tower2.manage_flight("second hello")

print(tower1 is tower2)