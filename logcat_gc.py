#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

count = 0
allocCount = 0

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
    cmd = "adb logcat -v time"
    logcat = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 使用管道
    while not logcat.poll():
        log = logcat.stdout.readline()
        line = str(log, encoding="utf-8").lower()
        if(isGC(line, pid)):
            count += 1
            if(isAlloc(line)):
                allocCount += 1
            print("all: " + str(count) + " , alloc:" + str(allocCount) + " , " + str(log, encoding="utf-8").strip())

if __name__ == '__main__':
    if(len(sys.argv) == 1):
        checkLogcat("")
    else:
        checkLogcat(sys.argv[1])
