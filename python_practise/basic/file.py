>>> import os
>>> os.name # 操作系统类型

'''
如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

要获取详细的系统信息，可以调用uname()函数：
'''
os.uname()

'''注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
'''

'''
在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
'''
os.environ

#要获取某个环境变量的值，可以调用os.environ.get('key')：

os.environ.get('PATH')

'''操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
'''

#查看当前目录的绝对路径
os.path.abspath('.')

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join('/users/michael','testdir')

#然后创建一个目录
os.mkdir('users/michael/testdir')

#删掉一个目录
os.rndir('user/michael/testdir')

#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.split('/User/michael/testdir/file.txt')
#('/User/micheal/testdir','file.txt')
#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
os.path.splitext('/path/to/file.txt')
#('path/to/file','.txt')

#对文件重命名
os.rename('test.txt','test.py')

#删文件
os.remove('test.py')

#最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
[x for x in os.listdir('.') if os.path.isdir(x)]

#要列出所有的.py文件，也只需一行代码：
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#序列化 （picklinkg/serialization marshalling flattening）

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
'''pickle.dumps()方法把任意对象序列化成一个bytes，然后，
就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象
序列化后写入一个file-like Object：
'''
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

'''当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()
方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python
命令行来反序列化刚才保存的对象：
'''
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()

#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：

import json
d = dict(name='Bob',age=20,score=858)
json.dumps(d)
#{'age':20,'score':88,'name':'Bob'}

#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

#要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

json_str = '{'age':20,'score':88,'name':'Bob'}'
json.loads(json_str)
