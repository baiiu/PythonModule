#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys


def readFiles(rootDir):
    if not os.path.exists(rootDir):
        return;

    filePaths=[];

    for (dirpath, dirnames, filenames) in os.walk(rootDir):
        # print(dirpath,filenames)
        for filename in filenames:
            # print(os.path.join(dirpath, filename));
            filePaths.append(os.path.join(dirpath, filename))

    return filePaths;



# 2. 遍历文件，读取内容，并封装成对象
def readInfos(filePaths):
    if(len(filePaths) == 0):
        return None;

    overImageInfos = [];
    for path in filePaths:
        # print(path);

        with open(path, 'r') as f:
            str = f.read()
            # print(json)
            overImageInfo = json.loads(str);
            # print(type(overImageInfo))
            # print(overImageInfo)
            overImageInfos.append(overImageInfo)

    return overImageInfos;


# 3. 按照url去重，虽然一般不会有重复文件
def distinct(items):
    urls = set()
    result = []
    for item in items:
        url = item['url']
        if url not in urls:
            urls.add(url)
            result.append(item)
    return result



# 5. 输出文件
def output(path, items):
    dirPath = os.path.dirname(path);
    filePath = os.path.join(dirPath,"output.json");

    f = open(filePath,'w');
    f.write(json.dumps(items))
    f.close()


if __name__ == '__main__':
    overImagePath = sys.argv[1]

    filePaths = readFiles(overImagePath)

    overImageInfos = readInfos(filePaths)

    # 去重
    overImageInfos = distinct(overImageInfos)

    # 排序
    overImageInfos.sort(key=lambda k: (k.get('scale', 0)), reverse=True)

    output(overImagePath,overImageInfos)
