#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Description:所有超过240天的文件从源目录移动到目标目录。

import shutil, sys, time, os, argparse

# argparse 是 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息。当然，Python 也有第三方的库可用于命令行解析，而且功能也更加强大，比如 docopt，Click。

usage = 'python move_file_if_over.py -src [SRC] -dst [DST] -days [DAYS]'
description = 'Moce files from src to dst if they are older than certain number of days.Default is 240days'

args_parser = argparse.ArgumentParser(usage=usage, description=description)
args_parser.add_argument('-src', '--src', type=str, nargs='?', default='.', help='(OPTIONAL) Directory where files will be moced from')
args_parser.add_argument('-dst', '--dst', type=str, nargs='?', required=True, help='(REQUIRED) Directory where files will be moced from')
args_parser.add_argument('-days', '--days', type=int, nargs='?', default=240, help='(OPTIONAL) Directory where files will be moced from')
args = args_parser.parse_args()

if args.days < 0:
    args.days = 0

src = args.src  #设置源目录
dst = args.dst  #设置保存目标目录
days = args.days  #设置天数
now = time.time() #获取操作时间 

if not os.path.exists(dst):
    os.mkdir(dst)

for f in os.listdir(src):  #遍历文件
    if os.stat(src+'/'+f).st_mtime < now - days * 86400:
        shutil.move(src+'/'+f, dst)  #移动文件
    else:
        print('没有超过目标天数')