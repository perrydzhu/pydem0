#!/usr/bin/env python
from terminal import Terminal
from time import sleep


def repeat_line(line):
    print(term.ERASE_BOL + term.UP + term.ERASE_EOL + line + term.NORM)



term = Terminal()
num = 0

print "[ App running... ]"

while True:
    line = "Tick: " + str(num)
    if num % 10:
        repeat_line(line)
    else:
        print(term.GREEN + line + term.NORM)

    sleep(0.5)
    num += 1


