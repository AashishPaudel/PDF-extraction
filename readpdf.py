# Importing required modules
import PyPDF2
# Creating a pdf file object
pdfFileObj = open('MT202.pdf','rb')

# Creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Getting number of pages in pdf file
pages = pdfReader.numPages

# Loop for reading all the Pages
for i in range(pages):

        # Creating a page object
        pageObj = pdfReader.getPage(i)

        # Printing Page Number
        print("Page No: ",i)

        # Extracting text from page
        # And splitting it into chunks of lines
        text = pageObj.extractText().split("  ")

        # Finally the lines are stored into list
        # For iterating over list a loop is used
        for i in range(len(text)):

                # Printing the line
                # Lines are seprated using "\n"
                print(text[i])

        # For Seprating the Pages
        print()

# closing the pdf file object
pdfFileObj.close()