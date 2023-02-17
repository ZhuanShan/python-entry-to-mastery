favorite_languages = {
    'jen':'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + 
        ",I see is " + 
        favorite_languages[name].title() + "!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you")

for language in set(favorite_languages.values()):
    print(language.title())


aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:    #前5个外星人
    print(alien)
print("...")

print("total number of aliens: " + str(len(aliens)))



aliens = []
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)
print("...")