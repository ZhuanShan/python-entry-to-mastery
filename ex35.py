from sys import exit

def gold_room ():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    #if choice.isdigit():
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
#当你输入taunt bear时，elif next == "taunt bear" and not bear_moved:的条件为真，故执行
#print "The bear has moved from the door. You can go through it now."
#bear_moved = True
#注意，此时并不会执行elif next == "taunt bear" and bear_moved:下的函数
#           dead("The bear gets pissed off and chews your legs off.")
#因为bear_moved = False,条件next == "taunt bear" and bear_moved为假。
#第一次输入taunt bear后，有两种情况：
#1）循环继续执行，再次输入taunt  bear时，bear_moved = True, 条件next == "taunt bear" and bear_moved为真，
#转调到函数  dead("The bear gets pissed off and chews your legs off.")
#2)循环继续执行,输入open door，bear_moved = True, 条件next == "open door" and bear_moved为真，
#转跳到函数gold_room

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

#https://zhuanlan.zhihu.com/p/38143880
#https://blog.csdn.net/qq_41718357/article/details/83384455
#https://zhidao.baidu.com/question/507961719.html
#https://www.douban.com/note/640520760/
