import os
import sys

#filepath=:
rootdir = r'F:\Pandownload\dota dataset\train\labelTxt-v1.5\DOTA-v1.5_train'
for i in os.listdir(rootdir):
    path = os.path.join(rootdir,i)#文件地址
    print(path)    #打印地址
    txt = open(path)
    neirong = txt.read()
    #print(neirong)
    sha = r'F:\gr.txt'
    f = open(sha, 'a')
    f.write(neirong)
    f.close()
    #print(txt.read())




#将文件保存至指定文件夹

    for num in neirong:
        if num == "ship":
            print(neirong)
            break
        elif num == "harbor":
            print(neirong)
            break
        else:
            continue

#f.close()


#sha = r'F:\gr.txt'
#f = open(sha, 'w')
#f.write(neirong)
#print(txt.read())

##for dirs in os.walk("F:\Pandownload\dota dataset\train\part1\images"):
#    for file in files:
#        print os.path.join(root,file).decode('gbk').encode('utf-8')
##

#txt = open(filename)
#print(f"here's your file {filename}:" )
#print(txt.read())


#if
