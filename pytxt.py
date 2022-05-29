import requests
import pdfplumber
import re
import pandas as pd
path = 'mt202.pdf'
with pdfplumber.open(path) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

print(text)

new_message_re = re.compile()