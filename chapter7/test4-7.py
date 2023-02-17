""" # 7-4
prompt = "enter a intergrent"
prompt += "\nenter quit to end"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
 """

# 7-5
prompt = "\ntell me the age"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        message = int(message)
        if message <=0:
            print("error")
            continue
        elif message <= 3:
            print("free")
        elif message > 3 & message <= 12:
            print("10 d")