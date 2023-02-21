from user import User

class Admin(User):
    def __init__(self, first_name, last_name, privilages = []):
        super().__init__(first_name, last_name)
        self.privilages = privilages

    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage)

    




class Privilage():
    def __init__(self, privilage):
        self.privilage = ['can add post', 'can delete post']

    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage)

