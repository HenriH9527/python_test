#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Description:扫描当前目录和所有子目录并显示大小

import os, sys


try:
    directory = sys.argv[1]
except IndexError:
    sys.exit('Must provide an argument')

dir_size = 0
fsize_dir = {
    'Bytes' : 1,
    'kilobytes' : float(1) / 1024,
    'Megabytes' : float(1) / (1024 * 1024),
    'Gigabytes' : float(1) / (1024 * 1024 * 1024)
}

for (path, dirs, files) in os.walk(directory):
    for file in files:
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)
'''
os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。

os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。

path --所指的是当前正在遍历的这个文件夹的本身的地址
dirs --是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files --同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
'''

fsizeList = [str(round(fsize_dir[key] * dir_size, 2)) + " " + key for key in fsize_dir ]

if dir_size == 0:
    print("空的文件")
else:
    print(fsizeList)
    for units in sorted(fsizeList)[::-1]:
        print("文件大小:", units)