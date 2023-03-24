#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time
import re

CHECK_DURATION = 10 * 1 * 60

count = 0
backgroundStickyCount = 0
backgroundPartialCount = 0
backgroundFullCount = 0
SuspendingCount = 0
WaitForGcToCompleteCount = 0

# I/art     ( 6910): Background sticky concurrent mark sweep GC freed 19151(1234KB) AllocSpace objects, 8(128KB) LOS objects, 17% free, 5MB/7MB, paused 6.068ms total 25.711ms
# I art     : Background partial concurrent mark sweep GC freed 64053(3MB) AllocSpace objects, 8(284KB) LOS objects, 33% free, 31MB/47MB, paused 7.138ms total 234.191ms
def isGC(line, pid):
    try:
        if (len(pid) == 0):
            return "gc freed" in line or "suspending all threads took" in line or "waitforgctocomplete" in line
        else:
            return pid in line and ("gc freed" in line or "suspending all threads took" in line or "waitforgctocomplete" in line)
    except Exception as e:
        return False

def isBackgroundSticky(line):
    try:
        return "background sticky concurrent" in line
    except Exception as e:
        return False
def isBackgroundPartial(line):
    try:
        return "background partial concurrent" in line
    except Exception as e:
        return False
def isBackgroundFull(line):
    try:
        return "background full concurrent" in line
    except Exception as e:
        return False
def isSuspending(line):
    try:
        return "suspending" in line
    except Exception as e:
        return False
def isWaitForGcToComplete(line):
    try:
        return "waitforgctocomplete" in line
    except Exception as e:
        return False

def checkLogcat(pid):
    global count
    global backgroundStickyCount
    global backgroundPartialCount
    global backgroundFullCount
    global SuspendingCount
    global WaitForGcToCompleteCount

    while not logcat.poll():
        log = logcat.stdout.readline()
        line = str(log, encoding="ISO-8859-1").lower()
        if(isGC(line, pid)):
            count += 1;
            if(isBackgroundSticky(line)):
                backgroundStickyCount += 1
            if(isBackgroundPartial(line)):
                backgroundPartialCount += 1
            if (isBackgroundFull(line)):
                backgroundFullCount += 1
            if (isSuspending(line)):
                SuspendingCount += 1
            if (isWaitForGcToComplete(line)):
                WaitForGcToCompleteCount += 1
            print("total: " + str(count) + ", BackgroundSticky:" + str(backgroundStickyCount)
                + ", isBackgroundPartial:" + str(backgroundPartialCount)
                + ", isBackgroundFull:" + str(backgroundFullCount)
                + ", isSuspending:" + str(SuspendingCount)
                + ", isWaitForGcToComplete:" + str(WaitForGcToCompleteCount)
                + ", \n" + str(log, encoding="ISO-8859-1").strip())

        # if (time.time() - startTime > CHECK_DURATION):
        #     break;

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
