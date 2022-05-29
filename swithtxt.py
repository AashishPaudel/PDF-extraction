import PyPDF2
import re

object = PyPDF2.PdfFileReader("MT202.pdf")

NumPages = object.getNumPages()

String = "Message Identifier"

for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    ResSearch = re.search(String, Text)
    print(ResSearch)

    