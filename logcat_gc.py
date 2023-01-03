#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


def isGC(log):
    try:
        line = str(log, encoding="utf-8").lower()
        return ("dalvikvm" in line or "art" in line) and "gc" in line and "freed" in line and "paused" in line
    except Exception as e:
        return False

def checkLogcat():
    cmd = "adb logcat -v time"
    logcat = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 使用管道
    while not logcat.poll():
        log = logcat.stdout.readline()
        if(isGC(log)):
            print(log.strip())

if __name__ == '__main__':
    checkLogcat()
