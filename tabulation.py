import csv
from tabulate import tabulate
csv_file = open("van.csv")
csv_file_read = csv.reader(csv_file)

csv_file_read.close()
#data = [["Name", "Age", "Weight"],["Salman","23","43"],["Ali","20","70"]]

print tabulate(csv_file_read)