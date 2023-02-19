""" # 8-9

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

NY = ['zhangsan', 'lisi', 'wangwu']
show_magicians(NY) """

""" # 8-10

def make_great(magicians):
    for index in range(0,len(magicians)):
        magicians[index] = "make great " + magicians[index]

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

NY = ['zhangsan', 'lisi', 'wangwu']

make_great(NY)
show_magicians(NY) 
 """
# 8-11

def make_great(magicians,new):
    for index in range(0,len(magicians)):
        magicians[index] = "make great " + magicians[index]
    new = magicians
    return new

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
    
NY = ['zhangsan', 'lisi', 'wangwu']
new_NY = []

new_NY = make_great(NY[:],new_NY)       #接收返回的新的列表
show_magicians(NY)
show_magicians(new_NY)