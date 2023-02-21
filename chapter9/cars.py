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

    def upgrade_battery(self):
        if self.battery_size <= 85:
            self.battery_size = 85
            print("upgrading")


class ElectricCar(Car):
    def __init__(self, make, model, year):          # 初始化电动车的参数信息
        super().__init__(make, model, year)         # 将父类信息和子类进行关联
        self.battery_size = 70
        self.battery = battery()

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + " kwh battery.")
    
    def fill_gas_tank(self):
        print("this car does not need a gas tank")
    