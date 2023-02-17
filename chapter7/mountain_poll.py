responses = {}

polling_active = True

while polling_active:
    name = input("\nwhat's your name")
    response = input("which mountain do you like to climb today?")

    responses[name] = response
    repeat = input("other?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n ...polling result...")
for name, response in responses.items():
    print(name + " would like to climb " + response)