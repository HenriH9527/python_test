#错误处理
try:
	print('try...')
	r = 10 / int('1')
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
else:
	print('no error')
finally:
	print('finally...')                                                         
print('END')

#断言 assert
def foo(s):
	n = int(s)
	assert n != 0,'n is zero!'
	return 10 / n

def main():
	foo('0')
#main()
#logging
import logging
#logging.basicConfig(level=logging.WARNING)

s = '0'
n = int(s)

#logging.info('n = %d' % n)
#print(10 / n)

#pdb  命令行启动 python -m pdb ```

#pdb 设置断点
import pdb
k = '0'
n = int(k)
#程序运行到这里自动停止
pdb.set_trace()
print(10 / n)
