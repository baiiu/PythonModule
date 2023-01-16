#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time

CHECK_DURATION = 10 * 1 * 60

count = 0
allocCount = 0
logcat = 0
startTime = 0

def isGC(line, pid):
    try:
        if (len(pid) == 0):
            return ("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line
        else:
            return ("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line and pid in line
    except Exception as e:
        return False

def isAlloc(line):
    try:
        return "gc_for_alloc" in line
    except Exception as e:
        return False

def checkLogcat(pid):
    global count
    global allocCount

    while not logcat.poll():
        log = logcat.stdout.readline()
        line = str(log, encoding="utf-8").lower()
        if(isGC(line, pid)):
            count += 1
            if(isAlloc(line)):
                allocCount += 1
            print("all: " + str(count) + " , alloc:" + str(allocCount) + " , " + str(log, encoding="utf-8").strip())

        if (time.time() - startTime > CHECK_DURATION):
            break;

if __name__ == '__main__':
    os.system("""
        adb shell am start "snssdk1840://home/play_video?group_id=7189121860964043557\&content_type=5"
    """)
    time.sleep(5)

    cmd = "adb logcat -v time"
    logcat = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 使用管道
    startTime = time.time()
    if(len(sys.argv) == 1):
        checkLogcat("")
    else:
        checkLogcat(sys.argv[1])

    print("111111")
    logcat.kill()
