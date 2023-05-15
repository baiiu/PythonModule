#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 计算某一个线程的时间片，占该进程的时间片占比；
# 主要看调整线程优先级，对播放器的时间片的影响。

# 1. adb shell ls /proc/pid/task，列出所有线程
# 2. adb shell cat /proc/pid/task/tid/stat，列出所有线程的cpu状态
# 3. adb shell cat /proc/pid/stat, 列出该进程cpu状态
# 4. 进程的总Cpu时间processCpuTime = utime + stime + cutime + cstime
#    线程的总Cpu时间threadCpuTime = utime + stime + cutime + cstime
#    计算占比

import os
import sys
import subprocess

class Thread:
    name = ''
    pid = ''
    tid = ''
    utime = 0
    stime = 0
    cutime = 0
    cstime = 0
    priority = 0
    nice = 0

    totalTime = 0

    def __init__(self, pid, tid):
        self.pid = pid
        self.tid = tid

    def totalTime(self):
        return self.utime + self.stime + self.cutime + self.cstime

Threads = [];

def run_command(cmd):
    # print('cmd: ', cmd)

    try:
        out_bytes = subprocess.check_output(cmd, shell=True)
        out_text = out_bytes.decode('utf-8')
        return out_text
    except CalledProcessError:
        return

def list_threads(pid):
    cmd = 'adb shell ls /proc/' + pid + '/task'
    result = run_command(cmd)
    result = result.rstrip()
    tids = result.split('\n')
    print("there are " + str(len(tids)) + " threads")

    for i in range(len(tids)):
        thread = Thread(pid,tids[i])
        Threads.append(thread)

def calculate(process, result):
    arr = result.rstrip().split(' ')
    if (len(arr) < 19):
        print("process not calculate: " + process.name)
        return
    # print(arr)
    process.name = arr[1]
    process.utime = int(arr[13])
    process.stime = int(arr[14])
    process.cutime = int(arr[15])
    process.cstime = int(arr[16])
    process.priority = int(arr[17])
    process.nice = int(arr[18])



def getProcessCpu(process):
    cmd = 'adb shell cat /proc/' + process.pid + '/stat'
    result = run_command(cmd)
    calculate(process, result)

def getThreadCpu(process):
    cmd = 'adb shell cat /proc/%d/task/%d/stat' % ((int)(process.pid), int(process.tid))
    result = run_command(cmd)
    calculate(process, result)

def filterThread(process):
    return '-L' in process.name
    # return True

def getCpuTotalTime():
    cmd = 'adb shell cat /proc/stat'
    result = run_command(cmd)
    cpuLine = result.split('\n')[0].rstrip()
    cpuArr = cpuLine.split(' ')
    cpuTotalTime = 0
    for i in range (1,9):
        if (cpuArr[i].isdigit()):
            cpuTotalTime += (int)(cpuArr[i])
    return cpuTotalTime

if __name__=='__main__':
    pid = sys.argv[1]


    process = Thread(pid, pid)
    getProcessCpu(process)
    processTime = process.totalTime()

    cpuTotalTime = getCpuTotalTime()

    list_threads(pid)
    for i in range(len(Threads)):
        getThreadCpu(Threads[i])

    # print(type(processTime))

    print("processTime={}, cpuTotalTime={}, processCpu={:2.2%}".format(processTime, cpuTotalTime, processTime*100 / cpuTotalTime))

    for i in range(len(Threads)):
        thread = Threads[i]
        if (filterThread(thread)):
            str = "{},\t {}, \t {}, \t {:2.2%}, \t{:2.2%}".format(thread.name, thread.priority, thread.nice,
                thread.totalTime() / processTime,
                thread.totalTime()*100 / cpuTotalTime,
            )
            print(str)
