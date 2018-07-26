#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Description:在提供了前3个八进制之后，它将扫描最后的范围以寻找可用的地址

import os, sys, subprocess


filename = sys.argv[0]

if '-h' in sys.argv or '--h' in sys.argv or '--help' in sys.argv or '-help' in sys.argv:
    print('''
        You need to supply the first octets of address Usage:''' + filename + ''' 111.111.111
    ''')
    sys.exit(0)
else:
    if (len(sys.argv) < 2):
        sys.exit('You need to supply the first octets of the address of the address Usage:' + filename + '111.111.111')
    subnet = sys.argv[1]

    if os.name == 'posix':
        myping = 'ping -c 2'
    elif os.name in ('nt', 'doc', 'ce'):
        myping = 'ping -n 2'

    f = open('ping_' + subnet + '.log', 'w',encoding='utf8')
    for ip in range(2, 255):
        ret = subprocess.call(myping + str(subnet) + '.' + str(ip), shell=True, stdout=f, stderr=subprocess.STDOUT)
        if ret == 0:
            f.write(subnet + '.' + str(ip) + 'is alive' + '\n')
        else:
            f.write(subnet + '.' + str(ip) + 'did not respond' + '\n')
