import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("MT202.pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "Confirmed Date"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)