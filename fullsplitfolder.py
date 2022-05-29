import PyPDF2
import re
import os.path
from os import path
from PyPDF2 import PdfFileWriter,PdfFileReader
from datetime import date
today = str(date.today())
file="../MT202.pdf"
# open the pdf file
object = PyPDF2.PdfFileReader(file)
NumPages = object.getNumPages()
# get number of pages
Start = "Message Identifier"
End = "Confirmed Date"
# define keyterms
Start_pagenum =[]
End_pagenum =[]
folder_name = []
# empty lists for start and end pages
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    abc = PageObj.extractText() 
    Start_page = re.search(Start, abc)
    start_fname = abc.find("Transaction Reference:") 
    end_fname = abc.find("Related Reference:")
    if str.replace(abc[start_fname:end_fname],"Transaction Reference:","") is not "":
        folder_name.append(str.replace(abc[start_fname:end_fname],"Transaction Reference:",""))
    print (folder_name) 
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
                    if not path.exists(today + " " + folder_name[i]):
                        os.mkdir (today + " " + folder_name[i])
                    for k in range(Start_pagenum[i], End_pagenum[j]+1):                      
                        print (today + " " + folder_name[i]+"/new_file_name"+str(i)+"splitted.pdf")
                        with open(today + " " + folder_name[i]+"/new_file_name"+str(i)+"splitted.pdf","wb") as f:
                                new_pdf.addPage(read_file.getPage(k))
                                new_pdf.write(f)
                                k+=1
                                print("PDF splitted Successfully")
    except Exception as e:
        print(e)
    
    

