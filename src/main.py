from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl


dataCSV = input("Provide the path to the .csv file with the data: ")
dataDict = {}
reader = csv.DictReader(open(dataCSV), fieldnames=(
    "name", "id", "centre", "designation", "joinDate", "bank", "bankAccNum", "leaveBalance", "sickLeaves", "addedLeaves", "totalLeaveBalance", "lopDays", "basicSal", "hra", "travelAllowance", "bonus", "otPay", "totPay", "advanceIncome", "advanceDeduction", "advancePending", "netPay", "comments"))
for row in reader:
    print(row)
