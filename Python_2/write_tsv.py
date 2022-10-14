import csv
with open("outtest.csv","w") as csvfile:
  writer = csv.writer(csvfile,delimiter="\t")
  writer.writerow(["Name","Flavor","Color"])
  writer.writerow(["Apple","Sweet","Red"])
  writer.writerow(["Pretzel","Salty","Brown"])

with open("outtest2.csv","w") as csvfile:
    writer = csv.writer(csvfile,delimiter="\t")
    writer.writerow(["Name","Flavor","Color"])
    writer.writerow(["Apple","Sweet","Red,Yellow","bruised"])
    writer.writerow(["Pretzel","Salty","Brown"])
