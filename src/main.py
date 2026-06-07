import csv
import reportlab


dataCSV = input("Provide the path to the .csv file with the data: ")
dataDict = {}
reader = csv.DictReader(open(dataCSV), fieldnames=(
    "name", "id", "centre", "designation", "joinDate", "bank", "bankAccNum", "leaveBalance", "sickLeaves", "addedLeaves", "totalLeaveBalance", "lopDays", "basicSal", "hra", "travelAllowance", "bonus", "otPay", "totPay", "advanceIncome", "advanceDeduction", "advancePending", "netPay", "comments"))
for row in reader:
    print(row)
