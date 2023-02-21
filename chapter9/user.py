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