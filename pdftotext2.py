import PyPDF2
from PyPDF2 import PdfFileReader
pdfFileObj = open('MT202.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#pageObj = pdfReader.getPage (0)
abc= pdfReader.extractText(),end='\n'
start = abc.find("Transaction Reference")
end = abc.find("Related Reference")
print (start)
print (end)
print (abc[start:end])
pdfFileObj.close ()
