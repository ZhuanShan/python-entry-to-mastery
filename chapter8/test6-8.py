""" # 8-6

def city_country(city_name, country_name):
    return f"{city_name.title()}, {country_name.title()}"

print(city_country('beijing', 'china'))

# 8-7

def make_album(singer, album, music_num = ''):
    diction = {
        'name': singer, 
        'songs': album,

        }
    if music_num:
        diction['music_num'] = music_num
    return diction


print(make_album('a','sun'))
print(make_album('b','moon',12))
 """

# 8-8

def make_album(singer, album, music_num = ''):
    diction = {
        'name': singer, 
        'songs': album,

        }
    if music_num:
        diction['music_num'] = music_num
    return diction


while True:
    print("tell me the album")
    print("enter 'q' to exit")

    singer_name = input("tell me the singer_name")
    if singer_name == 'q':
        break

    songs_name = input("tell me the songs name")
    if songs_name == 'q':
        break

    songs_number = input("tell me the number")
    if songs_number == 'q':
        break

    album = make_album(singer_name, songs_name, int(songs_number))
    print(album)



