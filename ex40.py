class Song(object):    #class后定义了一个类，类名叫song，从object下继承

    def __init__(self, lyrics):    #对song完成了初始化，形参有两个，一个self，一个lyrics
        self.lyrics = lyrics       #将外部传来的lyrics赋值给self对象的lyrics属性

    def sing_me_a_song(self):      #定义sing_me_a_song变量，参数为self
        for line in self.lyrics:   #对在self.lyrics里的line
            print(line)            #依次输出line值

happy_baby = Song(["happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
