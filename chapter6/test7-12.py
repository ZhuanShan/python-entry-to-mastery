# 6-7
human0 = {
    'last':'zhou',
    'first': 'wei',
    'age': '25',
    'city': 'BJ',
}

human1 = {
    'last': 'jia',
    'first': 'zhenyu',
    'age': '27',
    'city': 'BJ',
}

people = [human0, human1]

for human in people:
    print(human)
    for key, value in human.items():
        print(f"{key} : {value}")
    

# 6-8
pets = []
for num in range(2):
    pet = {
        'type' : f"pet{num}",
        'master' : f"master{num}",  
    }
    pets.append(pet)
for pet in pets:
    print(pet['master'] + " has a " +  pet['type'])
