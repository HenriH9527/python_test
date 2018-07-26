#!/usr/bin/python
# -*- coding: UTF-8 -*-


#Description:这将遍历服务器列表并ping一下机器，如果它已经启动，它将加载putty会话，如果不是，它将通知您。

import os, subprocess
from time import strftime


def windows():
    f = open('server_startup_' + strftime('%Y-%m-%d') + '.log', 'a')
    for server in open('startup_list.txt', 'r'):
        ret = subprocess.call('ping -n 3 %s' % server, shell=True, stdout=open('NUL', 'w'), stderr=subprocess.STDOUT)
        if ret == 0:
            f.write('%s: is alive,loading puTTY session' % server.strip() + '\n')
        else:
            f.write('%s : did not respond' % server.strip() + '\n')
def linux():
    f = open('server_startup_' + strftime('%Y-%m-%d') + '.log', 'a')
    for server in open('startup_list.txt'):
        ret = subprocess.call('ping -c 3 %s' % server, sheel=True,stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        if ret == 0:
            f.write('%s:is alive' % server.strip() + '\n')
        else:
            f.write('%s : did not respond' % server.strip() + '\n')
if os.name == 'posix':
    linux()
elif os.name in ('nt', 'doc', 'ce'):
    windows()
else:
    print('not supported')