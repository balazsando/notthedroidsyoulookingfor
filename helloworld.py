#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("%s %s!" % ("Hello", sys.argv[1]))
else:
    print("Hello World!")
