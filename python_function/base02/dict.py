#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther:Awe H
'''
info = {"abc":123,"cdf":324,"asdf":45454,"sfas":345,"sfac":3423}
print(info)
info["水电费"] = 3432
del info['abc']
print(info)
info.pop('水电费')
print(info)
print(info.get('cdf'))
'''
av_catalog = {
    "欧美":{
        'www.youporn.com':['很多免费的，世界最大的','质量一般'],
        'www.pornhub.com':['很多免费的，也很大','质量高'],
        'lctmcdothistoyou.com':['多是自拍，高质量图片很多','资源不多，更新慢'],
        'x-art.com':['质量很高，真的很高','全部收费，屌丝绕过']
    },
    "日韩":{
        'tokyo-hot':['质量还不错，老品牌','听说是收费的'],
    },
    "大陆":{
        '1024':['全部免费，真好','服务器在国外，慢']
    }
}

av_catalog["大陆"]['1024'][1] = "可以再国内做镜像"
#print(av_catalog)
#print(av_catalog.values())
av_catalog.setdefault('taiwan',{'www.baidu.com':[1,2]})
#print(av_catalog)
#info.update() 更新 覆盖
#info.items()   #把字典转成列表
#info.fromkeys()  初始化一个新的字典 共享内存地址
#for i in av_catalog:
 #   print(i,av_catalog[i])

for k,v in av_catalog.items():
    print(k, v)
