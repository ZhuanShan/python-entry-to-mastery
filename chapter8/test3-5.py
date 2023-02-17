# 8-3

def make_shirt(size, words):
    print("the size of t-shirt is " + size + " ,words are: " + words)

make_shirt('m', 'china')


# 8-4

def make_shirt(size, words = 'I love python'):
    print("the size of t-shirt is " + size + " ,words are: " + words)

make_shirt('m')
make_shirt('L')
make_shirt('s', 'I love C')


# 8-5

def descrbe_city(city = 'Reykjavik' , country = 'Iceland'):
    print(city + " is in " + country)

descrbe_city()
descrbe_city('shanghai', 'china')
descrbe_city('NY', 'us')
