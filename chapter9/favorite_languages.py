from collections import OrderedDict

favorite_languages = OrderedDict()      #用Orderdict()创建一个空的有序字典，并存储在favorite_language中

favorite_languages['jen'] = 'python'    #python3.6之后字典默认有序
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
favorite_languages['a'] = 'A'
favorite_languages['b'] = 'B'
favorite_languages['c'] = 'C'
favorite_languages['a'] = 'D'

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + '.')