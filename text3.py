""" age = 23
message = "happy" + str(age) +"re Birthday "
print(message) """

""" bicycles =['trek', 'conad','redline', 'specl']
message = "my first bickcle was a" + bicycles[0].title()
print(message)
 """

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
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


requested_topping = ['mushrooms','green peppers', 'extra cheese']
for requst in requested_topping:
    if requst == 'green peppers':
        print("sorry,")
    else:
        print("adding " + requst)
print("\nfinish")