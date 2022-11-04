#!/usr/bin/env python3

# this script will take as input a list of individuals.
#

# step 1 open the file 'individuals.txt' or if you are advanced
# make the name of the input file a command line argument
inputfile = "individuals.txt"
individuals = []
num_cols = 3  # you could make this something the user passes in or computed from the data
with open(inputfile, "r") as input:
    for line in input:
        line = line.strip()
        print(line) # you need to change this to save the data in array individuals
        # now read in the individuals and add them to the array
        # individuals

 # now generate pairwise combination of all the individuals
combinations = []
for x in range(len(individuals)):
    for y in range(x, len(individuals)):
        print("indexes are {} and {}, change this code to get to the actual individual name".format(x, y))
        # combo = ... # do something here to make the string which combines names of the two individuals eg "AB"
        # add this string in the array combinations


# now print out the combinations in a matrix

# first print col headers
colheader=[""]  # can leave first col empty since it is for the rows
for col in range(1,num_cols+1):
    colheader.append("Col{}".format(col))

print(",".join(colheader))
i=1
# for row in range(0,len(combinations),num_cols):
#  start = i*num_cols
# . end.  = (i+1)*num_cols
#  print ",".join([ "Row{}".format(i),combinations[start:end] ])
#  i+=1


# do the same as above but randomize the list of combinations first
