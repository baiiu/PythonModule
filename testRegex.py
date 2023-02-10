#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

line = "02-10 10:41:42.699 e/mlogu   (11587): hook dvmmallocproxy: 12"
dvmmallocproxyPattern = re.compile(r'(?:dvmmallocproxy: )\d+')
toAllocPattern = re.compile(r'\d+')
strRet = dvmmallocproxyPattern.findall(line)[0]
toAllocCount = toAllocPattern.findall(strRet)[0]
print(strRet)
print(toAllocCount)
print("mlogU" in line and toAllocCount > 1000)
print("mlogu" in line)
print(int(toAllocCount) > 1000)
