import sys
import PyPDF2
from PyPDF2 import PdfFileWriter
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
        print (ExtractedContent)

def pdf_splitter(file,start,end):

    new_file_name = file.split(".")[0] + " " + "splitted.pdf"

    file = pdfReader#read pdf
    
    new_pdf = PdfFileWriter() #create write object
    start-=1
    try:
        with open(new_file_name,"wb") as f:
            for i in range(start, end):
              new_pdf.addPage(file.getPage(i))
              new_pdf.write(f)
              i+=1
            print("PDF splitted Successfully")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    pdf_reader(pdfFileObj)
    pdf_splitter()