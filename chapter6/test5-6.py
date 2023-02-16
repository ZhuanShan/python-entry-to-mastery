# 6-5
rivers = {
    'nile': 'egypt',
    'chang': 'china',
    'huang': 'china',
}

for river in rivers.keys():
    print(f"The {river.title()} runs through {rivers[river].title()}")
    print(river.title())
    print(rivers[river].title())

# 6-6
favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
potiential_peoples = ['phil','sarah','jen','edward','hao']
for potiential_people in potiential_peoples:
    if potiential_people in favorite_languages.keys():
        print("thank you")
    else:
        print("invite")
