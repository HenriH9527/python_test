#检查在用户目录下有没有该文件，如果没有 则创建

import os

MESSAGE = '文件已存在'
TESTDIR = 'testdir'

try:
    #os.path.expanduser('~') 返回用户的主目录 
    home = os.path.expanduser('~')
    print(home)

    if not os.path.exists(os.path.join(home, TESTDIR)): #os.path.join() 连接路径
        os.makedirs(os.path.join(home, TESTDIR))
    else:
        print(MESSAGE)

except Exception as e:
    print(e)