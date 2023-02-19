def greet_users(names):
    for name  in names:
        msg = "hello, " + name.title() + "!"
        print(msg)

usernames = ['haha', 'ty', 'margot']
greet_users(usernames)