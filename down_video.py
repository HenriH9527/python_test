# 运用aria2c 下载视频  aria2是一个轻量级的多协议和多源命令行 下载实用程序。它支持HTTP / HTTPS，FTP，SFTP， BitTorrent和Metalink。aria2可以通过内置的 JSON-RPC和XML-RPC接口进行操作。

#subprocess模块，就是子流程模块,运行生成新进程，并获取它们的返回值

import subprocess
import sys

#sys.argv[0] 表示程序本省 argv[1],argv[2]...表示程序外部引用的部分 
video_link, threads = sys.argv[1], sys.argv[2]

subprocess.run([
    "youtobe-dl",
    video_link,
    "--external-downloader",
    "aria2c",
    "--externam-downloader-args",
    "-x"+threads   
])
