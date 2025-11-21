# Builder Pattern 

# when to use ?
# --> when you want to build object dynamically 
# --> means if you have 6 fields in constructor but want to create object with 3 fields only
# for this you have to write comibinations of the constructor so to over come this problem 
# we use this builder pattern 

# why to use ?
# --> to ease the object creation part 
# --> self explanatory and simple methods 


class House:
    def __init__(self, bathrooms, bedrooms, kitchen, ground, balcony, garage, parking):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.kitchen = kitchen
        self.ground = ground
        self.balcony = balcony
        self.garage = garage
        self.parking = parking

    def __str__(self):
        return (f"House: {self.bathrooms} bathrooms, {self.bedrooms} bedrooms, "
                f"{self.kitchen} kitchen, ground={self.ground}, balcony={self.balcony}, "
                f"garage={self.garage}, parking={self.parking}")

class HouseBuilder:
    def __init__(self):
        self.bathrooms = 1
        self.bedrooms = 1
        self.kitchen = 1
        self.ground = False
        self.balcony = False
        self.garage = False
        self.parking = False

    def set_bathrooms(self, count):
        self.bathrooms = count
        return self

    def set_bedrooms(self, count):
        self.bedrooms = count
        return self

    def set_kitchen(self, count):
        self.kitchen = count
        return self

    def add_ground(self, flag):
        self.ground = flag
        return self

    def add_balcony(self, flag):
        self.balcony = flag
        return self

    def add_garage(self, flag):
        self.garage = flag
        return self

    def add_parking(self, flag):
        self.parking = flag
        return self

    def build(self):
        return House(self.bathrooms,
                     self.bedrooms,
                     self.kitchen,
                     self.ground,
                     self.balcony,
                     self.garage,
                     self.parking)

# Usage
house = (
    HouseBuilder()
    .set_bathrooms(2)
    .set_bedrooms(3)
    .add_balcony(True)
    .add_parking(True)
    .build()
)

print(house)

