# 8-12

def sandwich(*toppings):
    for topping in toppings:
        print('adding ' + topping)

sandwich('cheese', 'beef', 'lamb')

# 8-13

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('zhou', 'wei',
                             location = 'bj',
                             field = 'compu')
print(user_profile)


#8-14

def cars_info(brand, type, **other_info):
    conclusion_info= {}
    conclusion_info['brand'] = brand.title()
    conclusion_info['type'] = type.title()
    for key, value in other_info.items():
        conclusion_info[key] = value
    return conclusion_info

special_car = cars_info('audi', 'a4', location = 'changchun', price  = '30')
print(special_car)
