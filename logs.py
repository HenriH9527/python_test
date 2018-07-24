#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Description:脚本将搜索给定目录中的所有.log文件，使用指定的程序对其进行压缩，然后对其进行日期标记

import os
from time import strftime


logsdir = 'D:\\gitRepository\\abc'
zip_program = "zip.exe"

print(os.listdir(logsdir))
for files in os.listdir(logsdir):
    if files.endswith('.log'):
        files1 = files + '.' + strftime("%Y-%m-%d") + ".zip"
        print(files1)
        os.chdir(logsdir)
        os.system(zip_program + " " + files1 + "" + files)
        os.remove(files)