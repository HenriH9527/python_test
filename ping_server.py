#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#Description: 根据所提供的参数，该脚本将检测与该应用程序组关联的服务器。

import os, subprocess, sys

filename = sys.argv[0]

if '-h' in sys.argv or '--h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv:
    print('''
    您需要为要检测的服务器提供应用程序！
    ''')
    sys.exit(0)
else:
    if (len(sys.argv) < 3):
        sys.exit('\n您需要提供正确的应用')
    appgroup = sys.argv[1]
    site = sys.argv[2]

    if os.name == 'posix':
        myping = 'ping -c 2'
    elif os.name in ('nt', 'dos', 'ce'):
        myping = 'ping -n 2'
    
    if 'dms' in sys.argv:
        appgroup = 'dms'
    elif 'swaps' in sys.argv:
        appgroup = 'swaps'

    if '155' in sys.argv:
        site = '155'
    elif 'bromley' in sys.argv:
        site = 'bromley'

    logdir = os.getenv('logs')
    logfile = 'ping_' + appgroup + 'site' + '.log'
    logfilename = os.path.join(logdir, logfile)
    confdir = os.getenv('my_config')
    conffile = (appgroup + '_servers_' + site + '.txt')
    coffilename = os.path. join(confdir, conffile)

    f = open(logfilename, 'w')
    for server in open(conffilename):
        ret = subprocess.call(myping + server, shell=True, stdout=f, stderr = suprocess.STDOUT)

        if ret == 0:
            f.write(server.strip() + 'is alive' + '\n')
        else:
            f.write(server.strip() + 'did not respond' + '\n')
    print('\n你可以在日志中看到结果:'+ logfilename)

