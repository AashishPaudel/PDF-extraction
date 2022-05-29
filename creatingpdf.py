import abc
import PyPDF2
from PyPDF2 import PdfFileReader
from fpdf import FPDF
pdfFileObj = open('MT202.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)



pdf = FPDF()      

pdf.add_page()  

pdf.set_font("Arial", size = 15)

f = open(abc) 

for x in f: 
    pdf.cell(50,5, txt = x, ln = 1, align = 'C') 

pdf.output("extracted.pdf")

def pdf_reader(pdfFileObj):
    for i in range(0,12):
        pageObj = pdfReader.getPage(i)
        abc= pageObj.extractText()

        start = abc.find("Message Identifier")
        end = abc.find("Confirmed Date")
        print (start)
        print (end)
        print (abc[start:end])

if __name__ == '__main__':
    pdf_reader(pdfFileObj)

