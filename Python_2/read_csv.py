import csv
file2 = "test2.csv"
with open(file2) as csvfile:
    reader = csv.reader(csvfile,delimiter=",")
    for row in reader:
        #print(row[1])
        print("\t".join(row[1:3]))

