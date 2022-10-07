#!/usr/bin/python3
# a comment
# a comment
import sys
import re

def main():


    for line in sys.stdin:
        m = re.match('^\s*#.*$',line)
        if m:
            continue
        print(line)

    print("got to here")

main()
