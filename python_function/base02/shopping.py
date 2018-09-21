#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

product_list = [
    ('iphoneX', 8000),
    ('Mac Pro', 12000),
    ('blueTooth', 800),
    ('kindle', 1200),
    ('coffaa', 30),
    ('surface', 8000)
]
shopping_list = []
salary = input('输入您要充值的金额：')
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index+1,item)
        user_choice = input("你要买啥捏？>>>")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                print(p_item)
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balabce is \033[01;31;40m%s\033[0m" % (p_item,salary))
                else:
                    print("\033[1;31;40m你的余额只剩%s啦，还买个毛线\033[0m" % salary)
            else:
                print('product code [%s] is not exist' % user_choice)
        elif user_choice == 'q':
            print('---------shopping list----------')
            for p in shopping_list:
                print(p)
            print('Your current balance:',salary)
            exit()
        else:
            print('invalid option!')
else:
    print('请输入正确的金额！')
