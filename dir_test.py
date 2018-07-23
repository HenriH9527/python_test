#!/usr/bin/python3

#首先我们需要明白该句语句是python2的概念，那么python3对于python2就是future了，也就是说，在python2的环境下，超前使用python3的print函数。
from __future__ import print_function

#测试目录testdir 是否存在  如果不存在，它将为你创建目录

import os
import sys

def main():

    Check_dir = input('输入你要查找的目录:')

    if os.path.exists(Check_dir):
        print('目录已存在')
    else:
        print('没有找到：%s' % Check_dir)
        print()
        os.makedirs(Check_dir)
        print('已创建目录：%s' % Check_dir)

if __name__ == '__main__':
    main()
