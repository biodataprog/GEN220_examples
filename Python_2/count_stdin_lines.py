#!/usr/bin/env python3

import sys # this tells python we need to use a package called sys
i=0
line=""
print("I'm on line",i,"the current text is",line)
for line in sys.stdin:
    print("I'm on line",i,"the current text is",line,
          end = '')
    i +=1