def greet_user():
    print("hello")

greet_user()

def greet_user(username):
    print("hello, " + username.title() + "!")

greet_user('jesse')


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("tell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last name")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nhello " + formatted_name)
