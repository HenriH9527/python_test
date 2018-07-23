#!/usr/bin/python3


#引入要用的包
#os.chdir  : 将当前工作目录更改为 Path
from os import chdir
import requests
#Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库
from bs4 import BeautifulSoup
#urllib 是读取，解析url的一个库
from urllib.request import urlopen, Request
from urllib.parse import urlencode
#os.walk : 通过自顶向下或自底向上遍历树来生成目录树中的文件名。对于位于目录顶部(包括顶部本身)的树中的每个目录，它会生成一个3元组(dirpath、dirname、filenames)。
from os import walk
#引用当前目录的常量字符串
from os.path import curdir
import json
from urllib.request import urlretrieve
from os.path import pardir
from create_dir import create_directory

GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

WALLPAPERS_KRAFT = 'https://wallpaperscraft.com/search/keywords?'

#设置代理头
usr_agent = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'none',
    'Accept-language':'en-US,en;q=0.8',
    'Connection':'keep-alive'
}

def image_grabber(ch):
    #从谷歌下载图片
    if ch == 1:
        print('Enter data to download Images:')
        data = input()
        search_query = {'q':data}
        search = urlencode(search_query)
        print(search)
        g = GOOGLE_IMAGE + search
        request = Request(g, headers = usr_agent)
        r = urlopen(request).read()
        sew = BeautifulSoup(r, 'html.parser')
        images = []
        # print(sew.prettify())
        results = sew.findAll('div',{"class":"rm_meta"})
        for re in results:
            link, Type = json.loads(re.text)["ou"], json.loads(re.text)["itf"]
            images.append(link)
        counter = 0
        for re in images:
            rs = requests.get(re)
            with open('img' + str(counter) + '.jpg', 'wb') as file:
                file.write(rs.content)
                counter += 1
        return True
    
    elif ch ==2:
        cont = set()  #存储图像的连接
        temp = set()  #优化链接以下载图片

        print('Enter data tp download wallpappers:')
        data = input()
        search_query = {'q':data}
        search = urlencode(search_query)
        print(search)
        g = WALLPAPERS_KRAFT + search
        request = Request(g, headers = usr_agent)
        r = urlopen(request).read()
        sew = BeautifulSoup(r, 'html.parser')
        count = 0
        for links in sew.find_all('a'):
            if 'wallpaperscraft.com/download' in links.get('href'):
                cont.add(links.get('href'))
        for re in cont:
            temp.add('https://wallpaperscraft.com/image/' + re[31:-10] + '_' + re[-9:] + '.jpg')
        
        #点击链接下载高清图片

        for re in temp:
            rs = requests.get(re)
            with open('img' + str(count) + 'jpg', 'wb') as file:
                file.write(rs.content)
            count += 1
        return True

    elif ch == 3:
        for folders, subfolder, files  in walk(curdir):
            for folder in subfolder:
                print(folder)
        return True
    elif ch == 4:
        print('Enter the directory to be set:')
        data = input()
        chdir(data + ':\\')
        print('Enter name for the folder:')
        data = input()
        create_directory(data)
        return True
        
    elif ch == 5:
        print('''
        -------------***Thank You For Using***-------------------
        ''')
        return False
run = True

print('''
*************{First Creating Folder To Save Your Image}****************
''')

create_directory('Images')
DEFAULT_DIRECTORY = pardir + '\\Images'
chdir(DEFAULT_DIRECTORY)

while run:
    print('''
    ------------Welcome-------------------
    1.寻找图片
    2.下载1080P墙纸
    3.查看目录中的图片
    4.设置文件夹
    5.退出
    ''')
    choice = input()
    run = image_grabber(int(choice))