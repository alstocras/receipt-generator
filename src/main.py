import csv

dataCSV = input("Provide the path to the .csv file with the data: ")

reader = csv.DictReader(open(dataCSV))
