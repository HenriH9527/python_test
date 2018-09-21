from multiprocessing import Process
import os


#子进程要执行的代码
'''def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))


#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个
#Process实例，用start()方法启动，这样创建进程比fork()还要简单。

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child process will start')
	p.start()

#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

	p.join()
	print('Child process end.')
'''
'''
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(6):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()

#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
#调用close()之后就不能继续添加新的Process了。

	p.join()
	print('ALL subprocesses done.')
'''
#很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

#subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''

#进程间通信

#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块
#包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

#以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

from multiprocessing import Process, Queue
import os, time, random

#写数据进程的代码
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

#读数据进程执行的代码：
def read(q):
	print('Process to read:%s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	#父进程创建Queue，并传给各个子进程：
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	#启动子进程pw,写入
	pw.start()
	#启动子进程pr,读取
	pr.start()
	#等待pw结束
	pw.join()
	#pr是死循环，无法等待结束，只能强行终止
	pr.terminate()
