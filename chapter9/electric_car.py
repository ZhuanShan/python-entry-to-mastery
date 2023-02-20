class Car():
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading  = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("full")


class ElectricCar(Car):
    def __init__(self, make, model, year):          # 初始化电动车的参数信息
        super().__init__(make, model, year)         # 将父类信息和子类进行关联
        self.battery_size = 70
        self.battery = battery()

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + " kwh battery.")
    
    def fill_gas_tank(self):
        print("this car does not need a gas tank")
    

class battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + " kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270
        
        message = "this car go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


    







my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
"""my_audi = Car('audi', 'a4', '2001')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_audi.fill_gas_tank() """
my_tesla.battery.get_range()