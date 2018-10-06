# import packages

from PyPDF2 import PdfFileReader
import re

path = '/Users/Navid/Documents/books'
book = 'progit.pdf'

pdf = PdfFileReader(path + f'/{book}')
# print(pdf)
number_of_pages = pdf.getNumPages()

# define keyterms
String = "\w*Install\w*"

# extract text and do the search

i = 0
while i < number_of_pages:
    PageObj = pdf.getPage(i)
    Text = PageObj.extractText()
    ResSearch = re.search(String, Text)
    if ResSearch is not None:
        print('p: ', i + 1, 'Found!')
    else:
        print('p: ', i + 1, '---')

    i += 1
