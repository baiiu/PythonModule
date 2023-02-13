#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

dvmmallocproxyPattern = re.compile(r'(?:dvmmallocproxy: )\d+')
toAllocPattern = re.compile(r'\d+')

def isLogU(line):
    try:
        strRet = dvmmallocproxyPattern.findall(line)[0]
        toAllocCount = toAllocPattern.findall(strRet)[0]
        print(strRet +", " + toAllocCount)
        return "mlogu" in line and int(toAllocCount) > 1000
    except Exception as e:
        return False


def isGC(line):
    ret1 = "dalvikvm" in str(line) or "art" in str(line)
    ret2 = isLogU(line)
    # print(ret1)
    # print(ret2)
    return ret1 or ret2

string1 = "02-10 10:41:42.699 e/mlogu   (11587): hook dvmmallocproxy: 1001"
string2 = "D/dalvikvm( 8374): GC_CONCURRENT freed 2000K, 17% free 67323K/80584K, paused 13ms+17ms, total 168ms"
print(isGC(string1))
print(isGC(string2))
