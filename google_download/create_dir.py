#引入要用到的包

from shutil import copytree
from shutil import move
from os import chdir
from os.path import exists
from os.path import pardir
from os import makedirs
from os import removedirs
from os import rename


#创建一个文件
def create_directory(name):
    if exists(pardir+"\\"+name):
        print('文件夹已存在，不能重写')
    else:
        makedirs(pardir+"\\"+name)

#删除文件
def delete_directory(name):
    removedirs(name)

#重命名文件
def rename_directory(direct, name):
    rename(direct, name)

#设置工作目录
def set_working_directory():
    chdir(pardir)

#备份文件夹树
def backup_files(name_dir, folder):
    copytree(pardir, name_dir + ':\\' + folder)

#移动文件到指定位置
#如果文件存在，重写它
def move_folder(filename, name_dir, folder):
    if not exists(name_dir+":\\"+folder):
        makedirs(name_dir+":\\"+folder)
    move(filename, name_dir+":\\"+folder+"\\")


'''
测试

def main():
    create_directory('test')
    rename_directory('test','demo')
    backup_files('D', 'backup_project')
    delete_directory('demo')
    move_folder('demo','D','names')


if __name__ == '__main__':
    main()
'''