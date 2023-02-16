""" age = 23
message = "happy" + str(age) +"re Birthday "
print(message) """

""" bicycles =['trek', 'conad','redline', 'specl']
message = "my first bickcle was a" + bicycles[0].title()
print(message)
 """

""" motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) """

""" motorcycles[0] = 'dukadi'
print(motorcycles) """
""" motorcycles.append('dukadi')
print(motorcycles) """
""" motorcycles.insert(0, 'dukadi') """
""" del motorcycles[0]
print(motorcycles) """

""" poped = motorcycles.pop(1)
print(motorcycles)
print(poped) """

""" motorcycles.remove('yamaha') """


""" motorcycles.sort(reverse=True) """
""" print(sorted(motorcycles))
print(motorcycles)
 """

""" for motorcycle in motorcycles:
    print(motorcycle) """

""" for value in range(1,5):
    print(value) """

""" numbers = list(range(2,6,2))
print(numbers) """

""" squares = []
for(value) in range(1,11):
    square = value**2
    squares.append(square)
print(squares) """

""" print("here are the three first player :")
for play in motorcycles[:2]:
    print(play.title()) """

""" friend = motorcycles[:]
print(friend) """


""" dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
 """

""" bannes_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in bannes_users:
    print(user.title()+ ", you can post a response if you wish") """

""" age = 19
if age >=18:
    print("you are too old") """

""" age = 17
if age >=18:
    print("you are too old")
else:
    print("sorry") """


""" requested_topping = ['mushrooms','green peppers', 'extra cheese']
for requst in requested_topping:
    if requst == 'green peppers':
        print("sorry,")
    else:
        print("adding " + requst)
print("\nfinish")
 """

""" available_toppings = ['mushroom', 'olive','green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding  "+ requested_topping)
    else:
        print("sorry")
print("\nfinish") """


""" alien_0 = {'color':'green','points':5} """

""" print(alien_0['color'])
print(alien_0['points']) """

""" new_points = alien_0['points']
print("you just "+ str(new_points)+ " points") """

""" alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
 """


""" alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print("original x_position:" + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x-position:" + str(alien_0['x_position'])) """


""" favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("sarah's favorite language is "+ 
    favorite_languages['sarah'].title()+
    "."
) """


user_0 = {
    'username':'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nkey: " + key)
    print("\nvalue:" + value)