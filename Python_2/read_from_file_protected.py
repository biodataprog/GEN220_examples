#!/usr/bin/env python3
i=0
file = "data1.dat"

with open(file,"r") as fh:
    for line in fh:
        print("line[%d] is %s"%(i,line),
            end = '')
        i+=1
