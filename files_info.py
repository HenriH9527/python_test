#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import os, sys, time, stat
'''
os.stat()返回值为：

st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。

'''

try_count = 16

while try_count:
    file_name = input('输入文件名：')
    fhand = open(file_name, 'r', encoding='UTF-8')
    count = 0
    for lines in fhand:
        count = count + 1
    fhand = open(file_name, 'r', encoding='UTF-8')
    inp = fhand.read()
    t_char = len(inp)
    try_count >>= 1
    try:
        file_stats = os.stat(file_name)
        print('该文件的详细信息',file_stats)
        break
    except OSError:
        print('no file')

if try_count == 0:
    print('超出权限 退出程序')
    sys.exit()
'''
Python程序有两种退出方式： os._exit() 和 sys.exit()。我查了一下这两种方式的区别。

os._exit() 会直接将python程序终止，之后的所有代码都不会执行。

sys.exit() 会抛出一个异常: SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获该异常的代码，那么这些代码还是会执行。
'''

#创建一个文件保存文件信息

file_info = {
    'fname' : file_name,
    'fsize' : file_stats[stat.ST_SIZE],
    'f_lm' : time.strftime("%Y/%m/%d %I:%M:%S %p", time.localtime(file_stats[stat.ST_MTIME])),
    'f_la' : time.strftime("%Y/%m/%d %I:%M:%S %p", time.localtime(file_stats[stat.ST_ATIME])),
    'f_ct' : time.strftime("%Y/%m/%d %I:%M:%S %p", time.localtime(file_stats[stat.ST_CTIME])),
    'no_of_lines' : count,
    't_char' : t_char
}

print('\n文件名：', file_info['fname'])
print('\n文件大小：', file_info['fsize'])
print('\n文件修改时间：', file_info['f_lm'])
print('\n文件最近访问时间：', file_info['f_la'])
print('\n文件创建时间：', file_info['f_ct'])
print('\n文件的行数：', file_info['no_of_lines'])
print('\n文件字节数：', file_info['t_char'])

if stat.S_ISDIR(file_stats[stat.ST_MODE]):
    print('这是个目录')
else:
    print('这不是个目录')

'''
S_ISLNK(st_mode)：是否是一个连接.
S_ISREG(st_mode)：是否是一个常规文件.
S_ISDIR(st_mode)：是否是一个目录
S_ISCHR(st_mode)：是否是一个字符设备.
S_ISBLK(st_mode)：是否是一个块设备
S_ISFIFO(st_mode)：是否 是一个FIFO文件.
S_ISSOCK(st_mode)：是否是一个SOCKET文件 
'''