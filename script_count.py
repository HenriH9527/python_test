#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Descripiton: 扫描我的脚本目录，并给出不同类型脚本的计数

import os


path = os.getenv('/scripts')
dropbox = os.getenv('/dropbox')

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('CLS')

def count_files(path, extensions):
    counter = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            counter += file.endswith(extensions)
    return counter

def github():
    github_dir = os.path.join(dropbox, '/github')
    github_count = sum((len(f) for _,_, f in os.walk(github_dir)))

    if github_count > 5:
        print('\nYou have too many in here , start uploading!!')
        print('You have:' + str(github_count) + 'waiting to be uploaded to github')
    elif github_count == 0:
        print('\nGithub directory is all clear')
    else:
        print('\nYou have' + str(github_count) + 'waiting to be uploaded to github')

def development():
    dev_dir = os.path.join(path, '/development')
    dev_count = sum((len(f) for _,_, f in os.walk(dev_dir)))
    if dev_count > 10:
        print('\n You have too many in here, finish them or delete them!!')
        print('You have: ' + str(dev_count) + 'waiting to be finished!')
    elif dev_count == 0:
        print('\n Development directory is all clear')
    else:
        print('You have: ' + str(dev_count) + 'waiting to be finished!')


if __name__ == '__main__':
    clear_screen()
    development()