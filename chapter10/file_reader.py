with open('F:\pythonfile\practise\chapter10\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())            #rstrip()消除多余空白行

file_name = 'F:\pythonfile\practise\chapter10\pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


file_name = 'F:\pythonfile\practise\chapter10\pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()         #readlines从文件中读取每一行并存到列表中

for line in lines:
    print(line.rstrip())