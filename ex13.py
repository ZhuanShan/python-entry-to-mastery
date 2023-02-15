from sys import argv
#sys 为内置模块，提供了许多函数和变量来处理 Python 运行时环境的不同部分。是固定的用法，
#不能自己随便写名字代替它，这行的作用就是要把用到的东西（比如需要什么特定函数什么之类的）从这个东西存放的模块中引入程序中。
#rgv就是列表（参数变量），是编程术语。在解释器启动后, argv 列表包含了传递给脚本的所有参数, 第一个元素为脚本自身的名称。
#read the Wyss section for how to run this
script,first,second,third=argv

print("the script is called:", script)
print("your first variable is:",first)
print("Your second variable is:",second)
print("your third variable is:",third)
