import PyPDF2
import fpdf
from PyPDF2 import PdfFileReader

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

        print (ExtractedContent)

        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Helvetica", size=8)

        for i in ExtractedContent:
            print(i)
            pdf.write(5,ExtractedContent)
            pdf.output("hello00.pdf")
        

if __name__ == '__main__':
    pdf_reader(pdfFileObj)

