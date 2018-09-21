#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

anime = {
    '火影':{
        '鸣人':{'螺旋丸'},
        '佐助':{'须佐能乎'},
        '卡卡西':{'千鸟','隐分身'}
    },
    '海贼王':{
        '路飞':{'橡皮枪'},
        '娜美':{'气候棒'},
        '驯鹿':{'医术'}
    },
    '犬夜叉':{
        '犬夜叉':{'铁碎牙'},
        '大少爷':{'天生牙'},
        '弥勒':{'黑洞'}
    }
}

while True:
    for i in anime:
        print(i)
    choice = input('选择你喜欢的动漫>>>：')
    if choice in anime:
        while True:
            for j in anime[choice]:
                print(j)
                choice2 = input('选择进入能力库：')
                if choice2 in anime[choice]:
                    while True:
                        for k in anime[choice][choice2]:
                            print('\t\t',k)
                            choice3 = input('选择进入')
                            if choice3 in anime[choice][choice2]:
                                for m in anime[choice][choice2][choice3]:
                                    print('\t\t',m)
