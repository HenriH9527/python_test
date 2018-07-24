#!/usr/bin/python

#这个脚本用来检查是否设置了我需要的所有环境变量

import os


confdir = os.getenv("my_config")
conffile =str('env_check.conf')
conffilename = os.path.join(confdir, conffile)

print(confdir)

for env_check in open(conffilename):
    env_check = env_check.strip()
    print('[{}]'.format(env_check))
    newenv = os.getenv(env_check)

    if newenv is None:
        print(env_check,'没有设置')
    else:
        print('Current Setting for {}={}'.format(env_check, newenv))