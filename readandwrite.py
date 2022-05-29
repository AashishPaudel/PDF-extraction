import PyPDF2
from PyPDF2 import PdfFileReader
from reportlab.lib.colors import Blacker, black
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
pdfFileObj = open('MT202.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

def pdf_reader(pdfFileObj):
    for i in range(0,12):
        pageObj = pdfReader.getPage(i)
        abc= pageObj.extractText()

        start = abc.find("Message Identifier")
        end = abc.find("Confirmed Date")
        q = (abc[start:end])
        ExtractedContent = str(q)
        print (start)
        print (end)
        print (q)
        
        canvas = Canvas("newfile"+str(i)+".pdf", pagesize=LETTER)
# Set font to Times New Roman with 12-point size
        canvas.setFont("Times-Roman", 12)
# Draw blue text one inch from the left and ten
# inches from the bottom
        canvas.setFillColor(black)
        Story=[]
        print (ExtractedContent)
        styles=getSampleStyleSheet()
        Story.append(Paragraph(str(q), styles["Normal"]))
        
# Save the PDF file
        canvas.save()
if __name__ == '__main__':
    pdf_reader(pdfFileObj)

