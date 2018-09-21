#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

count = 0
while True:
    print('count:', count)
    count = count + 1
    if count == 1000:
        break
#带参数  3表示步长
for i in range(0,10,3):
    print('loop',i)

for i in range(0,10):
    if i < 5:
        print('loop',i)
    else:
        continue
    print('hehe...')
for i in range(10):
    print('-------',i)
    for j in range(10):
        print(j)
