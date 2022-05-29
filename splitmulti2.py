import PyPDF2
import re
import sys
from PyPDF2 import PdfFileWriter,PdfFileReader


# open the pdf file
object = PyPDF2.PdfFileReader("MT202.pdf")

# get number of pages
NumPages = object.getNumPages()

# define keyterms
Start = "Message Identifier"
End = "Confirmed Date"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    abc = PageObj.extractText() 
    # print(Text)
    ResSearch = re.search(Start, abc)
    ResSearch = re.search(End, abc)
    print(ResSearch)

def pdf_splitter(file,start,end):
    
    new_file_name = file.split(".")[0] + " " + "splitted.pdf"

    read_file = PdfFileReader(open(file,"rb")) #read pdf
    
    new_pdf = PdfFileWriter() #create write object
    start-=1
    try:
        with open(new_file_name,"wb") as f:
            for i in range(start, end):
              new_pdf.addPage(read_file.getPage(i))
              new_pdf.write(f)
              i+=1
            print("PDF splitted Successfully")
    except Exception as e:
        print(e)


if len(sys.argv) < 4:
    print("*"*50)
    print("Invalid Agruments")
    print("-"*50)
    print("python splitmulti.py pdf_file_name_with_full_path start_page_number end_page_number")
    print("-"*50)
    print("Example")
    print("python splitmulti.py 'hello.pdf' 2 5")
    print("*"*50)
else:
    file_path = object
    start_page = int(sys.argv[2]) #start page number 
    end_page = int(sys.argv[3]) #end page number
    pdf_splitter(file_path,start_page,end_page)