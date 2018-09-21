#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

names = "zhangyang zhangfei guanyu liubei lvbu"
names = ['zhangyang','zhangfei','guanyu','liubei','lvbu']
names.append('sunwukong') #后排插入
names.insert(1,'fengbao') #任意位置插入
names[2] = "mingren" #修改
names.remove('mingren') #删除
del names[0]  #删除
names.pop()  #默认删除最后一个值
print(names)
print('-----',names[2])
print('0-2',names[0:-1:3])  #切片
print(names.index('guanyu'))
