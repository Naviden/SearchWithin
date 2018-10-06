# import packages

from PyPDF2 import PdfFileReader
import re


pdf = PdfFileReader('clojureforthebraveandtrue.pdf')
number_of_pages = pdf.getNumPages()


# define keyterms
String = "package"


# extract text and do the search
# for i in range(0, number_of_pages):
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
