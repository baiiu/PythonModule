#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os,re

print('=============================================')
print('5. upload the apk')
print('=============================================')


formData = {'type':'android','bundle_id':'com.com.baiiu.zhihudaily','api_token':'05ecd7ec7bc11ca209752fdaeb2f8cb6'}
response = requests.post('http://api.fir.im/apps', data = formData)
# print(response.text)
data = response.json()
icon = data['cert']['icon']
binary = data['cert']['binary']
print(icon['key'])
print(binary['key'])


# 现在的问题主要是如何获取 versionName 和 versionCode,icon
# 1. 直接调用java解析apk包,python得需要配置很多东西去依赖能解压apk包的东西
# 2. python调用aapt反编译
# 3. 依赖androguard


def uploadIcon(requestUrl,key,token,file):
    formData={'key':key,'token':token,'file':'05ecd7ec7bc11ca209752fdaeb2f8cb6'}



# data = {
#     'name': 'nginx'
# }
# files = {'file': open("abc.csv", 'rb')}
#
# response = requests.post(url, data=data, files=files)
