class Restraurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisin_type = type
        self.set_number_served = 0

    
    def describe_restaurant(self):
        print("the name of restaurant is " + self.restaurant_name.title())
        print("type of restraurant is " + self.cuisin_type.title())
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")
    
    def read_number_served(self):
        print(str(self.set_number_served) + " have eatting in this")