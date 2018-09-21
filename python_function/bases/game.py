#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H

count = 0
age_of_oldboy = 56

while count < 3:
    guess_age = int(input('guess age:'))
    if guess_age == age_of_oldboy:
        print('yes,you got it')
        break
    elif guess_age > age_of_oldboy:
        print('think smaller...')
    else:
        print('think bigger!')
    count += 1
else:
    print('you have tried too many times...get fuck off!')
