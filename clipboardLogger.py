# -*- coding: UTF-8 -*-
import pyperclip
import sys
import time

def logger_callback(logLocation):
    counter = 1
    clipper = ""
    file = open(logLocation, "a+", encoding='utf-8')
    timer_add = 0;
    while (1):
        if (pyperclip.paste()!=clipper):
            clipper = pyperclip.paste()
            file.write("{0} {1}\n".format(counter, clipper))
            counter += 1
        time.sleep(0.5)
        timer_add += 0.5
        if (timer_add > 2):
            timer_add = 0
            file.flush()
            print("write for once into {0}".format(logLocation))

if __name__ == '__main__':
    logger_callback(sys.argv[1])