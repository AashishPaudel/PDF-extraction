import PyPDF2
from PyPDF2 import PdfFileReader
pdfFileObj = open('MT202.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

def pdf_reader(pdfFileObj):
    for i in range(0,12):
        pageObj = pdfReader.getPage(i)
        abc= pageObj.extractText()

        start = abc.find("Transaction Reference:")
        end = abc.find("Related Reference:")
        print (abc[start:end])

if __name__ == '__main__':
    pdf_reader(pdfFileObj)
