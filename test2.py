import os
import sys
import shutil



#def search_f(imgdir,sname):
#    for i in os.listdir(imgdir):
#        if sname in i:
#            shutil.copy(imgdir,r"F:\tyn") #新图片位置
#    return



#filepath=:
rootdir = r'F:\ty'    #原标签位置 (改)
for i in os.listdir(rootdir):
    path = os.path.join(rootdir,i)#文件地址
    print(path)    #打印地址
    txt = open(path)
    neirong = txt.read()
    #print(neirong)

    spnei = (neirong.split( ))
    #print(spnei)
    wenjian = os.path.splitext(i)[0]
    for num in spnei:
        if num == "ship" or num == "harbor":  #要获取的标签（改）
            print(wenjian)
            shutil.copy(path,r"F:\tyn")    #新标签位置（改）

#拷贝图片
            imgdir = r"F:\imd"           #原图片位置
            for r in os.listdir(imgdir):
                impath = os.path.join(imgdir,r)
                if wenjian in r:
                    shutil.copy(impath,r"F:\imdn")    #新图片位置（改）

            break                        #跳出for循环，打印没有后缀的文件名


#rootdir原标签位置
#path标签的根地址
#txt打开标签
#neirong标签内容
#spnei标签分割
#wenjian标签文件名（没有后缀）
#impath图片的跟地址
