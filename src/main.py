from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

outfile = "generations/payslip.pdf"

template = PdfReader("assets/template.pdf", decompress=False).pages[0]
templateObj = pagexobj(template)

canvas = Canvas(outfile)

objName = makerl(canvas, templateObj)
canvas.doForm(objName)

canvas.drawString(200, 298, "no")

canvas.save()
