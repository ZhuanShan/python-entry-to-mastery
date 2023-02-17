# 7-8
sandwich_orders = ['cheese', 'beef', 'lamp']
finished_sandwichs = []

while sandwich_orders:
    current_making = sandwich_orders.pop()
    print("I made your " + current_making + " sandwich")
    finished_sandwichs.append(current_making)

print("the following sandwich have been made: ")
for finish in finished_sandwichs:
    print(finish.title())


# 7-9
sandwich_orders = ['cheese', 'pastrami', 'beef','pastrami', 'lamp', 'pastrami']
print("pastrami has sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)


# 7-10
responses = {}
polling_active = True

while polling_active:
    name = input("\nwhat's your name")
    response = input("where would you like to go")
    responses[name] = response
    repeat = input("yes or no")
    if repeat == 'no':
        polling_active = False

print("\n ...result...")
for name, response in responses.items():
    print(name + " would like to " + response )