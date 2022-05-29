import PyPDF2
import re
from PyPDF2 import PdfFileWriter,PdfFileReader


file="MT202.pdf"
# open the pdf file
object = PyPDF2.PdfFileReader(file)


NumPages = object.getNumPages()
# get number of pages

Start = "Message Identifier"
End = "Confirmed Date"
# define keyterms

Start_pagenum =[]
End_pagenum =[]
# empty lists for start and end pages


for i in range(0, NumPages):
    PageObj = object.getPage(i)
    abc = PageObj.extractText() 
    Start_page = re.search(Start, abc)
    
    if(Start_page is not None):
        Start_pagenum.append(i)
    print(Start_pagenum)

    end_page=re.search(End,abc)
    
    if(end_page is not None):
        End_pagenum.append(i)
    print(End_pagenum)

    read_file = PdfFileReader(open(file,"rb")) #read pdf
    
    try:
         for i in range(0, len(Start_pagenum)):
            for j in range(0, len(End_pagenum)):          
                if i==j:
                    new_pdf = PdfFileWriter()
                    with open("new_file_name"+str(i)+"splitted.pdf","wb") as f:
                        for k in range(Start_pagenum[i], End_pagenum[j]+1):
                            new_pdf.addPage(read_file.getPage(k))
                            new_pdf.write(f)
                            k+=1
                            print("PDF splitted Successfully")
    except Exception as e:
        print(e)
    
    

