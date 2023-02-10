#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time
import re

CHECK_DURATION = 10 * 1 * 60

count = 0
allocCount = 0
concurrentCount = 0
logcat = 0
startTime = 0


dvmmallocproxyPattern = re.compile(r'(?:dvmmallocproxy: )\d+')
toAllocPattern = re.compile(r'\d+')

def isLogU(line):
    strRet = dvmmallocproxyPattern.findall(line)[0]
    toAllocCount = toAllocPattern.findall(strRet)[0]
    return "mlogu" in line and int(toAllocCount) > 1000

def isGC(line, pid):
    try:
        if (len(pid) == 0):
            return isLogU(line) or (("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line)
            # return (("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line)
        else:
            return pid in line and (isLogU(line) or (("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line))
            # return pid in line and ((("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line))
    except Exception as e:
        return False

def isAlloc(line):
    try:
        return "gc_for_alloc" in line
    except Exception as e:
        return False

def isConcurrent(line):
    try:
        return "gc_concurrent" in line
    except Exception as e:
        return False


def checkLogcat(pid):
    global count
    global allocCount
    global concurrentCount

    while not logcat.poll():
        log = logcat.stdout.readline()
        line = str(log, encoding="ISO-8859-1").lower()
        if(isGC(line, pid)):
            count += 1;
            if(isAlloc(line)):
                allocCount += 1
            if(isConcurrent(line)):
                concurrentCount += 1
            print("total: " + str(count) + ", alloc:" + str(allocCount) + ", concurrent" + str(concurrentCount) + ", " + str(log, encoding="ISO-8859-1").strip())

        if (time.time() - startTime > CHECK_DURATION):
            break;

if __name__ == '__main__':
    # os.system("""
    #     adb shell am start "snssdk1840://home/play_video?group_id=7189121860964043557\&content_type=5"
    # """)
    # time.sleep(5)

    os.system("adb logcat -c")

    cmd = "adb logcat -v time"
    logcat = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 使用管道
    startTime = time.time()
    if(len(sys.argv) == 1):
        checkLogcat("")
    else:
        checkLogcat(sys.argv[1])
