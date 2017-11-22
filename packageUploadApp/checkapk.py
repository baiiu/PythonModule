#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,re

def getAppBaseInfo(apkpath):
    #检查版本号等信息
    output = os.popen("./aapt d badging %s" % apkpath).read()

    # package: name='com.baiiu.routerdesignlearn' versionCode='1' versionName='1.0' platformBuildVersionName='7.1.1'
    matchVersion = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)' platformBuildVersionName='\S+'").match(output)
    if not matchVersion:
        raise Exception("can't get packageinfo")

    # packagename = matchVersion.group(1)
    versionCode = matchVersion.group(2)
    versionName = matchVersion.group(3)


    # application: label='RouterDesign' icon='res/mipmap-mdpi-v4/ic_launcher.png'

    iconName = ''

    outList = output.split('\n')
    for line in outList:
        if line.startswith('application: label'):
            matchIcon = re.compile("application: label='(\S+)' icon='(\S+)'").match(line)
            # print('label: ' + matchIcon.group(1))
            # print('iconName: ' + matchIcon.group(2))
            iconName = matchIcon.group(2)

    return versionCode,versionName,iconName


def getCurrentDirApk():
    for dir in os.walk(os.path.dirname(__file__)):
        for filename in dir[2]:
            if os.path.splitext(filename)[1] == '.apk':
                print('find apk:', filename)
                return filename

if __name__ == "__main__":
    #获得apk名
    apkName = getCurrentDirApk()

    if not apkName:
        print('can not find apk!!!')
        exit()

    os.chdir(os.path.dirname(__file__))
    versionCode,versionName,iconName = getAppBaseInfo(apkName)
    print('versionCode: ' + versionCode)
    print('versionName: ' + versionName)
    print('iconName: ' + iconName)
