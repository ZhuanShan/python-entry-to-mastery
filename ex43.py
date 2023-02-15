from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and imlement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
	"You died .You kinda suck at this.你死了。你有点不好意思",
	"Your mom would be pound...if she were smarter.如果她更聪明，你的妈妈会感到自豪",
	"such a luser.这样的失败者",
	"I have a small puppy that's better at this.我有一只小狗在这方面做得更好",
	"You're worse than you Dad's jokes.你比你爸爸的笑话更糟糕"
	]

    def enter(self):
        print(Death.quips[randit(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
			The Gothons of planet Percal #25 haveinvaded your ship and
			desteoyed your entire crew.You are the last surviving
			member and your last mission is to get the neutron destruct
			bomb from the Weapons Armory, put it in the bridge, and
			blow the ship up afther getiing into an escape pod .

			You're running down the central corridor to the Weapons
			Armory when a Gothon jumps out , red scaly skin, dark grimy
			filled body . He's blocking the door to the Armory and
			about topull a weapon blast you.行星Percal＃25的Gothons已经侵入
			你的船并使你的整个船员消失。你是最后一个幸存的成员，你的最后一个任务
			是从武器军械库获得中子毁灭炸弹，把它放在桥上，然后把船吹起来 当Gothon
			跳出来时，你正沿着通往武器军械库的中央走廊向下跑，红色的鳞状皮肤，充满
			黑暗肮脏的身体。 他正在阻挡军械库的大门，以及一个武器爆炸你。
			"""))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
				Quick on the draw you yank out your blaster and fire
				it at the Gothon . His clown costume is flowing and
				moving around his body, which throws off you aim .
				This completely ruins his brand new costume but misses him entirely
				bought him, which makes him fly into an insane rage
				and blast you repeatedly in the face untill you are
				dead . Then he eats you. 快速抽签你猛拉你的冲击波并在Gothon上开火。 他的
				小丑服装在他的身体周围流动和移动，这让你失去了目标。这完全破坏了他的全新服装
				，但是错过了他完全买了他，这使他飞入疯狂的愤怒中并反复爆炸你的脸，直到你死了
				。 然后他吃了你。
				"""))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
				Like a world class boxes you dodge, weave, slip and
				slide right as the Gothon's blaster cranks a laser
				past your head. In the middle of your artful dodge
				your foot slips and you bang your head on the metal
				wall and pass out. You wake up shortly after only to
				die as the Gothon stomps on your head and eats you.
				就像一个世界级的盒子，你躲闪，编织，滑动和当Gothon的冲击波
				发出激光时，向右滑动过了你的脑袋。 在你巧妙的躲闪中间你的脚滑
				了，你的头撞在金属上墙和传递出去。 你很快就醒来了当Gothon踩到
				你的头上并吃掉你时死去。
				"""))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
				Lucky for you they made you learn Gothon insults in
				the acadmy. You tell one Gothon joke you konw:
				Lbhe zbgure vf fb sng , jura fur fvgf nebhaq gur ubhfr,
				jura fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
				not to laugh, then busts out laughing and can't move.
				While he's laughing you run up and shoot him square in
				Weapon Armory door.幸运的是，他们让你学会了Gothon在学院里的
				侮辱。 你告诉一个Gothon笑话你知道：Lbhe zbgure vf fb sng，jura
				 fur fvgf nebhaq gur ubhfr，jura fur fvgf nebhaq gur ubhfr。
				 Gothon停了下来，尽量不笑，然后大笑起来，不能动弹。虽然他笑了，但
				 他跑起来，在武器军械库门口射击他。
				"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
			You do a dive roll into the Weapon Armory, crouch and scan
			the room for more Gothons that might be hiding. It's dead
			quiet, too quiet . You stand up and run to the far side of
			the room and find the neutron bomb in its container.
			There's akeypad lock on the box and you need the code to
			get the bomb out. If you get hte code wrong 10 times then
			the lock closes forever and you can't get the bomb. The
			code is 3 digits .你进入武器军械库潜水，蹲伏并扫描房间以寻找
			可能隐藏的更多Gothons。 它很安静，太安静了。 你站起来跑到房间的
			另一边，在它的容器里找到了中子炸弹。盒子上有一个akeypad锁，你需要
			代码来取出炸弹。 如果你的代码错误10次，那么锁会永远关闭，你无法得
			到炸弹。 代码是3位数。
			"""))

        code = f"{randint(1, 9)} {randint(1, 9)} {randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
				The container clicks open and the seal breaks, letting
				gas out. You grab the neutron bomb and run as fast as
				you can to he bridge whrer you must place it in the
				right spot.容器咔嗒一声打开，密封破裂，让气体排出。 你抓住中
				子弹并尽可能快地跑到桥上，你必须将它放在正确的位置。
				"""))
            return 'the_bridge'
        else:
            print(dedent("""
				The lock buzzes one last time and then you hear a
				sickening melting sound as the mechanism is fused
				together. You decide to sit there, and you die .
				锁最后一次发出嗡嗡声，然后当机制融合在一起时，你会听到
				令人作呕的融化声。 你决定坐在那里，你死了。
				"""))
            return 'death'

class TheBridge(Scene):

	def enter(self):
		print(dedent("""
			You burst onto the Bridge with the netron destruct bomb
			under your arm and surprise 5 Gothons who are trying to
			clown costume than the last. They haven't pulled their
			weapons out yet, as they see the active bomb under your
			arm and don't want to set it off.你用手臂下的netron destruct
			炸弹冲上了大桥，让5个正在努力的Gothons感到惊讶比上一个小丑服装。
			他们没有拉他们的武器还没出来，因为他们看到了你身上的活跃炸弹手臂，
			不想把它关掉。
			"""))
		action = input(">")

		if action == "throw the bomb":
			print(dedent("""
				In a panic you throw the bomb at the group of Gothons
				and make a leap for the door. Right as you drop it a
				Gothon shoots you right in the back killing you. As
				you die you see anthoer Gothon frantically try to
				disarm the bomb. You die knowing they will probably
				blow up when it goes off.在恐慌中，你将炸弹扔到Gothons
				集团并向门进行跳跃。 就在你放下它的时候，Gothon会在后面向
				你射击，杀死你。 当你死去的时候，你会看到蚂蚁Gothon疯狂地
				试图解除炸弹的武装。 你知道他们可能会在它熄火时爆炸。
				"""))
			return 'death'
		elif action == "slowly place the bomb":
			print(dedent("""
				You point your blaster at the bomb under your arm and
				the Gothons put thei hands up and start to sweat .
				You inch backward to the door, open it ,and then
				carefully place the bomb on the floor, pointing your
				blaster at it . you then jump back through the door,
				punch the close button and blast the lock so the
				Gothon can't get out . Now that the lock so the
				Gothons can't get out. Now that the bomb is placed
				you run to the escape pod to get off this tin can.
				你把你的冲击波指向你手臂下的炸弹，而Gothons把你的手举起来
				开始出汗。你向后靠近门，打开它，然后小心翼翼地将炸弹放在地板
				上，指着你的冲击波。 然后你跳回门，按下关闭按钮并敲开锁，这样
				Gothon就无法离开。 既然锁定让Gothons无法脱身。 现在炸弹被放置
				，你跑到逃生舱下车这个锡罐。
				"""))
			return 'escape_pod'
		else:
			print("DOES NOT COMPUTE")
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print(dedent("""
			You rush through the ship desperaely trying to make it to
			the escapr pod before the whole ship explodes. It seems
			like hardly any Gothons are on the ship, so your run is
			clear of interference. You get to the chamber with the
			escape pods ,and now need to pick one to take. Some of
			them could be damage but you don't have time to look.
			There's 5 pods, which one do you take?在整艘船发生爆炸之前，
			你绝望地冲过船只试图进入逃生舱。 似乎几乎没有任何Gothons在船上，
			所以你的奔跑没有干扰。 你带着逃生舱到达房间，现在需要选择一个。
			其中一些可能是损坏，但你没有时间去看。有5个逃生舱，你选哪一个？
			"""))

		good_pod = randint(1,5)
		guess = input("[pod #]>")

		if int(guess)!=good_pod:
			print(dedent("""
				You jump into pod {guess} and hit the eject button.
				The pod escapes out into the viod of space, then
				implodes as the hull ruptures, crushing your body
				into jam jelly.你跳进pod {guess}然后点击弹出按钮。
				吊舱逃离空间，然后随着船体破裂爆炸，将身体压碎成果冻果冻。
				"""))
			return 'death'
		else:
			print(dedent("""
				You jump into pod {guess} and hit the ejeck button.
				The pod easily sildes out into space heading to
				the planet below. As it flies to the planet, you look
				back and see your ship implode then explide like a
				bright star, taking out the Gothon ship at the same
				time.You won!你跳进了pod {guess}并点击了ejeck按钮。这个
				吊舱很容易滑入太空，前往下面的星球。 当它飞向地球时，你回头
				看看你的船内爆然后像一颗明亮的星星一样探索，同时取出Gothon
				船。你赢了！
				"""))
			return 'finished'

class Finished(Scene):

	def enter(self):
		print("You won! Good job.")
		return 'finished'

class Map(object):

	scenes = {
	'central_corridor':CentralCorridor(),
	'laser_weapon_armory':LaserWeaponArmory(),
	'the_bridge':TheBridge(),
	'escape_pod':EscapePod(),
	'death':Death(),
	'finished':Finished(),
	}

	def __init__(self,start_scene):
		self.start_scene =start_scene

	def next_scene(self,scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')   #建立一个map类对象并赋予初始场景
a_game = Engine(a_map)  #.建立Engine类对象并将map类对象作为参数传入
a_game.play()               #开始游戏
