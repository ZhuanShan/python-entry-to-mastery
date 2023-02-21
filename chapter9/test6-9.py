# 9-6
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
    

class IceCreamStand(Restraurant):
    def __init__(self, name, type, flavors=[]):
        super().__init__(name, type)
        self.flavors = flavors


    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor)

my_favorite = Restraurant('kfc', 'us')
icestore = IceCreamStand('m ji', 'us',['juice', 'coke'])
icestore.describe_flavors()


# 9-7

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

class Admin(User):
    def __init__(self, first_name, last_name, privilages = []):
        super().__init__(first_name, last_name)
        self.privilages = privilages

    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage)

    
admin_name = Admin('zhang', 'san', ['can add post', 'can delete post'])
admin_name.show_privilages()



class Privilage():
    def __init__(self, privilage):
        self.privilage = ['can add post', 'can delete post']

    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage)

