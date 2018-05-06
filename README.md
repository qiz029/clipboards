# clipboard
This is a python based project intended to allow use to have multiple clipboards
Currently only support windows

This is the earliest version

date: 05-05-2018

Author: Todd_Zheng

Usage: 
- shift+F1/2/3/4/5+C will copy chosen text to the first clipboard
- shift+F1/2/3/4/5+V will paste chosen text to the first clipboard


###known issue

- Ctrl Q cannot quit
- The actual process is still very long

## Add clipboard Logger 
- This Component is for logging for the clipboard
- to use it, do ```python clipboardLogger.py {logLocation}```
- the Log will be in the format of {counter} {content}