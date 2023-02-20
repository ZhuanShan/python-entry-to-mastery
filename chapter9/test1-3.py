# 9-1 9-2

class Restraurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisin_type = type
    
    def describe_restaurant(self):
        print("the name of restaurant is " + self.restaurant_name.title())
        print("type of restraurant is " + self.cuisin_type.title())
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")
    
    

my_favorite = Restraurant('kfc', 'us')
my_favorite.describe_restaurant()
my_favorite.open_restaurant()


# 9-3

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nthe user's first name is " + self.first_name.title())
        print("\nthe user's last name is " + self.last_name.title())
    
    def greet_user(self):
        full_name = self.first_name.title() + self.last_name.title()
        print("\nhi " + full_name )

user_name = User('zhang', 'san')

user_name.greet_user()




