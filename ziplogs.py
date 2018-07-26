#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Description:  压缩给定目录中的所有日志

import os, shutil
from time import strftime

logsdir = "D:\\old files"
zipdir = "D:\\old files\\ziplogs"
zip_program = 'zip.exe'

for files in os.listdir(logsdir):
    print(files)
    if files.endswith('.log'):
        files1 = files + '.' + strftime('%Y-%m-%d') + '.zip'
        os.chdir(logsdir)
        os.system(zip_program + " " + files1 + " " + files)
        shutil.move(files, zipdir)
        os.remove(files)
        print(1)
