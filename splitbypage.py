import os
import PyPDF2
import re
import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileWriter
object = PyPDF2.PdfFileReader("MT202.pdf")

NumPages = object.getNumPages()

String = "Message Identifier"

for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    ResSearch = re.search(String, Text)

def pdf_splitter(object):
    fname = os.object.splitext(os.object.basename(object))[0]
    pdf = PdfFileReader(object)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    pdf_splitter(object)
