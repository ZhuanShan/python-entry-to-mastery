# 9-4
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
    

my_favorite = Restraurant('kfc', 'us')
my_favorite.set_number_served = 20
my_favorite.read_number_served()
my_favorite.describe_restaurant()
my_favorite.open_restaurant()


# 9-5

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("\nthe user's first name is " + self.first_name.title())
        print("\nthe user's last name is " + self.last_name.title())
    
    def greet_user(self):
        full_name = self.first_name.title() + self.last_name.title()
        print("\nhi " + full_name )

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_name = User('zhang', 'san')

for i in range(10):
    user_name.increment_login_attempts()

print(user_name.login_attempts)
user_name.reset_login_attempts()
print(user_name.login_attempts)
user_name.greet_user()