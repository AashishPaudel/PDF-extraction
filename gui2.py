import PyPDF2
import calendar;
import time;
import re
import tkinter as tk
import os.path
from os import path
from PyPDF2 import PdfFileWriter,PdfFileReader
from datetime import date
from tkinter import *
from tkinter import filedialog
import os
 
# root = Tk()
# root.title('Browse File')
# root.geometry('200x20')a
# root.config(bg='lightblue')
today = str(date.today())
file = filedialog.askopenfilename()
#print (file)
    
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
swift_Type = []
gmt = time.gmtime()
#print("gmt:-", gmt)
ts = calendar.timegm(gmt)
# empty lists for start and end pages
if not path.exists(str(ts)):
    os.mkdir (str(ts))
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    abc = PageObj.extractText() 
    Start_page = re.search(Start, abc)
    start_fname = abc.find("Transaction Reference:") 
    end_fname = abc.find("Related Reference:")
    #for identifying 3 digit code
    start_digit = abc.find("Unique Message Identifier") 
    end_digit = abc.find("Message Header")
    folder_digit = str.replace(abc[start_digit:end_digit],"Unique Message Identifier:","")
    swift_Type.append(folder_digit[14:18])
    print(swift_Type)
    if end_fname != "None":
        end_fname=abc.find("Priority:")
    if str.replace(abc[start_fname:end_fname],"Transaction Reference:","") is not "":
        folder_name.append(str.replace(abc[start_fname:end_fname],"Transaction Reference:",""))
        
    #print (folder_name) 
    if(Start_page is not None):
        Start_pagenum.append(i)
    #print(Start_pagenum)
    end_page=re.search(End,abc) 
    if(end_page is not None):
        End_pagenum.append(i)
    #print(End_pagenum)
    read_file = PdfFileReader(open(file,"rb")) #read pdf  
    try:
         for i in range(0, len(Start_pagenum)):
            for j in range(0, len(End_pagenum)):          
                if i==j:
                    new_pdf = PdfFileWriter()
                    #if not path.exists(today + " " + folder_name[i]):
                    #    os.mkdir (today + " " + folder_name[i])
                    for k in range(Start_pagenum[i], End_pagenum[j]+1):                      
                        #print (str(ts)+"/"+str(folder_name[i])+".pdf")
                        with open(str(ts)+"/"+str(folder_name[i])+"_"+str(swift_Type[i])+".pdf","wb") as f:
                                new_pdf.addPage(read_file.getPage(k))
                                new_pdf.write(f)
                                k+=1
    except Exception as e:
        print(e)
    print("PDF splitted Successfully")