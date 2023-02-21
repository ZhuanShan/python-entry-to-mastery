""" favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
} """

favorite_languages = {}
favorite_languages['jen'] = ['python']
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'haskell'
favorite_languages['a'] = 'A'
favorite_languages['b'] = 'B'
favorite_languages['c'] = 'C'
favorite_languages['a'] = 'D'

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())