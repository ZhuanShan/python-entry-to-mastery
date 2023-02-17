""" message = input("tell me ")
print(message)
 """

""" prompt = "\ntell me:"
prompt += "\nenter quit to end"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message) """


prompt = "\ntell me:"
prompt += "\nenter quit to end"
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)